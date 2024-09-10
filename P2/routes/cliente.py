from flask import Blueprint, render_template, request, redirect, url_for, flash,current_app ,send_file
from database.models.cliente import Cliente ,Profissional
import os
from werkzeug.utils import secure_filename
 

cliente_route = Blueprint('cliente', __name__)


@cliente_route.route('/cadastrar_profissional', methods=['POST'])
def cadastrar_profissional():
    if 'foto' not in request.files:
        return 'Nenhuma foto enviada', 400
    foto = request.files['foto']
    if foto.filename == '':
        return 'Nenhuma foto selecionada', 400

    # Verificar se o diretório existe, e se não, criá-lo
    upload_folder = os.path.join(current_app.root_path, 'static/uploads/profissionais')
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    # Salvar a foto no servidor
    caminho_foto = os.path.join(upload_folder, secure_filename(foto.filename))
    foto.save(caminho_foto)

    # Salvar os dados no banco de dados com o caminho relativo à pasta 'static'
    caminho_foto_relativo = 'uploads/profissionais/' + secure_filename(foto.filename)
    nome = request.form.get('nome')
    especialidade = request.form.get('especialidade')
    bio = request.form.get('bio')
    
    # Salvar no banco de dados
    novo_profissional = Profissional.create(nome=nome, especialidade=especialidade, bio=bio, foto=caminho_foto_relativo)
    
    return redirect(url_for('cliente.lista_profissionais'))



@cliente_route.route('/profissionais')
def lista_profissionais():
    profissionais = Profissional.select()  # Recupera todos os profissionais
    return render_template('profissionais.html', profissionais=profissionais)


@cliente_route.route('/profissional/<int:id>')
def detalhes_profissional(id):
    profissional = Profissional.get(Profissional.id == id)
    return render_template('detalhes_profissional.html', profissional=profissional)





@cliente_route.route('/cadastro', methods=['GET', 'POST'])
def inserir_cliente():
    if request.method == 'POST':
        nome = request.form.get('name')
        email = request.form.get('email')
        senha = request.form.get('password')

        try:
            Cliente.create(nome=nome, email=email, senha=senha)
            flash('Cadastro realizado com sucesso!', 'success')
            return redirect(url_for('home.index'))
        except Exception as e:
            flash(f'Erro ao cadastrar usuário: {e}', 'danger')
            return render_template('index.html')
    

@cliente_route.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('password')
        
        

        try:
            usuario = Cliente.get(Cliente.email == email, Cliente.senha == senha)
            return render_template('home.html')
        except Cliente.DoesNotExist:
            flash('Email ou senha incorretos.', 'danger')
            return render_template('index.html')
    

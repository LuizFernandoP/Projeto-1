from flask import Blueprint, render_template, request, redirect, url_for, flash,current_app ,send_file,session
from database.models.cliente import Cliente ,Profissional,Admin
import os
from werkzeug.utils import secure_filename
 

cliente_route = Blueprint('cliente', __name__)

@cliente_route.route('/cadastrar_profissional', methods=['GET','POST'])
def cadastrar_profissional():
    if request.method == 'POST':
        
        nome = request.form.get('name')
        email = request.form.get('email')
        senha = request.form.get('password')

        session['nome'] = nome
        session['email'] = email
        session['senha'] = senha

        
        return redirect(url_for('cliente.cadastrar_etapa2'))  
    
    return render_template('index2.html')

@cliente_route.route('/cadastrar_etapa2', methods=['GET', 'POST'])
def cadastrar_etapa2():
  if request.method == 'POST':

    if 'foto' not in request.files:
        return 'Nenhuma foto enviada', 400
    foto = request.files['foto']
    if foto.filename == '':
        return 'Nenhuma foto selecionada', 400

    
    upload_folder = os.path.join(current_app.root_path, 'static/uploads/profissionais')
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    
    caminho_foto = os.path.join(upload_folder, secure_filename(foto.filename))
    foto.save(caminho_foto)

    
    caminho_foto_relativo = 'uploads/profissionais/' + secure_filename(foto.filename)
    
    especialidade = request.form.get('especialidade')
    bio = request.form.get('bio')
    telefone=request.form.get('telefone')
    cep=request.form.get('cep')
    try:
      nome = session.get('nome')
      email = session.get('email')
      senha = session.get('senha')

      Profissional.create(
            nome=nome,
            especialidade=especialidade,
            bio=bio,
            foto=caminho_foto_relativo,
            email=email,
            senha=senha,
            telefone=telefone,
            cep=cep
        )
      flash('Cadastro realizado com sucesso!', 'success')
      return render_template('index2.html')
    except Exception as e:
            flash(f'Erro ao cadastrar profissional: {e}', 'danger')
            return render_template('index2.html')
    
  return render_template('cadastrar_profissional.html')

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
            return render_template('index.html')
        except Exception as e:
            flash(f'Erro ao cadastrar usuário: {e}', 'danger')
            return render_template('index.html')
    
    return render_template('index.html')

@cliente_route.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('password')

        try:
            usuario_admin = Admin.get(Admin.email == email, Admin.senha == senha)
            return redirect(url_for('cliente.admin_painel'))  
          
        except Admin.DoesNotExist:
            pass
        
        try:
            usuario_cliente = Cliente.get(Cliente.email == email, Cliente.senha == senha)
            return redirect(url_for('cliente.lista_profissionais')) 
        
        except Cliente.DoesNotExist:
            pass
        
    
        try:
            usuario_profissional = Profissional.get(Profissional.email == email, Profissional.senha == senha)
            return redirect(url_for('cliente.lista_profissionais')) 
            flash(f'Bem-vindo, {usuario_profissional.nome}!', 'success')
            
        except Profissional.DoesNotExist:
            flash('Email ou senha incorretos.', 'danger')
            return render_template('index.html')

    return render_template('index.html')
  
@cliente_route.route('/criar_admin')
def criar_admin():
    
    if Admin.select().where(Admin.is_admin == True).exists():
        return "Um administrador já existe!", 400
    
    novo_admin = Admin.create(nome="Admin", email="admin@gmail.com", senha="1234567", is_admin=True)
    
    return "Administrador criado com sucesso!"


@cliente_route.route('/admin_painel')
def admin_painel():

    
    
    profissionais = Profissional.select()
    
    return render_template('admin_painel.html', profissionais=profissionais)



@cliente_route.route('/delete_profissional/<int:id>', methods=['POST'])
def delete_profissional(id):
    
    profissional = Profissional.get(Profissional.id == id)
    profissional.delete_instance()
    return redirect(url_for('cliente.admin_painel'))

@cliente_route.route('/lista_clientes')
def lista_clientes():
    
    clientes = Cliente.select()
    return render_template('lista_clientes.html', clientes=clientes)


@cliente_route.route('/delete_cliente/<int:id>', methods=['POST'])
def delete_cliente(id):
   
    cliente = Cliente.get(Cliente.id == id)
    cliente.delete_instance()
    return redirect(url_for('cliente.lista_clientes'))

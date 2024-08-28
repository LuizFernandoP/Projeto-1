from flask import Blueprint, render_template, request, redirect, url_for, flash
from database.models.cliente import Cliente

cliente_route = Blueprint('cliente', __name__)

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
    

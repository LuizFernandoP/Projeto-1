from flask import Flask, render_template, request, redirect, url_for, flash
from flask import SQlite

app = Flask(_name)  #Corrigido de _name para _name_
app.secret_key = "chave_secreta"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'  #Configuração do banco de dados SQLite
db = SQlite(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(150), unique=True, nullable=False)
    senha = db.Column(db.String(150), nullable=False)

#Cria o banco de dados e as tabelas se não existirem
with app.app_context():
    db.create_all()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        usuario = request.form.get("usuario")
        senha = request.form.get("senha")
        confirmacao_senha = request.form.get("confirmacao_senha")
        
        if not usuario or not senha or not confirmacao_senha:
            flash("Todos os campos são obrigatórios", "danger")
            return redirect(url_for('register'))
        
        if senha != confirmacao_senha:
            flash("As senhas não coincidem", "danger")
            return redirect(url_for('register'))

        usuario_existente = Usuario.query.filter_by(usuario=usuario).first()
        if usuario_existente:
            flash("Usuário já existe", "danger")
            return redirect(url_for('register'))

        novo_usuario = Usuario(usuario=usuario, senha=senha)
        db.session.add(novo_usuario)
        db.session.commit()

        flash(f"Usuário {usuario} cadastrado com sucesso!", "success")
        return redirect(url_for('index'))

    return render_template("register.html")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get("usuario")
        senha = request.form.get("senha")
        
        if not usuario or not senha:
            flash("Todos os campos são obrigatórios", "danger")
            return render_template("index.html")

        usuario_registrado = Usuario.query.filter_by(usuario=usuario, senha=senha).first()

        if usuario_registrado:
            flash(f"Usuário {usuario} logado com sucesso!", "success")
            return redirect(url_for('index'))
        else:
            flash("Usuário ou senha incorretos", "danger")
            return render_template("index.html")

    return render_template("login.html")

@app.route('/recover', methods=['GET', 'POST'])
def recover():
    if request.method == 'POST':
        usuario = request.form.get("usuario")
        
        if not usuario:
            flash("O campo de usuário é obrigatório", "danger")
            return redirect(url_for('recover'))

        usuario_registrado = Usuario.query.filter_by(usuario=usuario).first()

        if usuario_registrado:
            flash(f"A senha para o usuário {usuario} é {usuario_registrado.senha}", "info")
            return redirect(url_for('index'))
        else:
            flash("Usuário não encontrado", "danger")
            return redirect(url_for('recover'))

    return render_template("recover.html")

if _name_ == '_main':  #Corrigido de _name para _name_
    app.run(debug=True)
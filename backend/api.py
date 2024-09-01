from flask import Flask, request, jsonify
from flask_cors import CORS
from peewee import SqliteDatabase, Model, CharField, ForeignKeyField
import random

# Configuração do banco de dados SQLite
db = SqliteDatabase('projeto1.db')

# Modelo das tabelas do banco de dados

# Modelo User
class User(Model):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db

# Modelo Acesso
class Acesso(Model):
    user = ForeignKeyField(User, backref='acessos', on_delete='CASCADE')
    codigo = CharField()

    class Meta:
        database = db

# Função para gerar o código padrão
def gerar_codigo_padrao():
    return str(random.randint(1000, 9999))  # Gera um código de 4 dígitos

# Inicializando o aplicativo Flask
app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

# Conectando ao banco de dados e criando as tabelas
db.connect()
db.create_tables([User, Acesso], safe=True)
db.close()

# Rota principal para verificar se a API está rodando
@app.route('/')
def index():
    return "API Rodando"

# Nova rota para adicionar usuários via parâmetros de formulário ou query string
@app.route('/api/adduser', methods=['POST'])
def add_user():
    name = request.form.get('name') or request.args.get('name')
    email = request.form.get('email') or request.args.get('email')
    password = request.form.get('password') or request.args.get('password')

    # Verifica se todos os parâmetros foram fornecidos
    if not name or not email or not password:
        return jsonify({'error': 'Todos os campos são obrigatórios: name, email, password'}), 400

    try:
        if User.select().where(User.email == email).exists():
            return jsonify({'message': 'Usuário já existe'}), 409

        # Criando o usuário e o acesso associado com código gerado automaticamente
        user = User.create(
            name=name,
            email=email,
            password=password
        )

        codigo = gerar_codigo_padrao()
        acesso = Acesso.create(
            user=user,
            codigo=codigo
        )

        return jsonify({
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'codigo': acesso.codigo
        }), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Rota para obter todos os usuários e seus códigos
@app.route('/api/getallusers', methods=['GET'])
def get_all_users():
    try:
        users = User.select()
        users_list = []
        for user in users:
            acessos = Acesso.select().where(Acesso.user == user)
            for acesso in acessos:
                users_list.append({
                    'id': user.id,
                    'name': user.name,
                    'email': user.email,
                    'codigo': acesso.codigo
                })
        return jsonify(users_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Implementando a rota de login
@app.route('/api/login', methods=['POST'])
def login():
    email = request.form.get('email') or request.args.get('email')
    password = request.form.get('password') or request.args.get('password')

    # Verifica se todos os parâmetros foram fornecidos
    if not email or not password:
        return jsonify({'error': 'Email e senha são obrigatórios'}), 400

    user = User.select().where(User.email == email).first()
    
    # Verifica se o usuário existe e se a senha está correta
    if user and user.password == password:
        return jsonify({'message': 'Login bem-sucedido'}), 200
    else:
        return jsonify({'message': 'Credenciais inválidas'}), 401
    
@app.route('/api/alterar_senha', methods=['POST'])
def alterar_senha():
    name = request.form.get('name') or request.args.get('name')
    email = request.form.get('email') or request.args.get('email')
    codigo = request.form.get('codigo') or request.args.get('codigo')
    new_password = request.form.get('new_password') or request.args.get('new_password')

    # Verifica se todos os parâmetros foram fornecidos
    if not name or not email or not codigo or not new_password:
        return jsonify({'error': 'Nome, email, código de acesso e nova senha são obrigatórios'}), 400

    try:
        # Verifica se o usuário e o email são válidos
        user = User.select().where(User.name == name, User.email == email).first()
        if user:
            # Verifica se o código de acesso está correto
            acesso = Acesso.select().where(Acesso.user == user, Acesso.codigo == codigo).first()
            if acesso:
                # Atualiza a senha do usuário
                user.password = new_password
                user.save()
                return jsonify({'message': 'Senha alterada com sucesso'}), 200
            else:
                return jsonify({'error': 'Código de acesso inválido'}), 401
        else:
            return jsonify({'error': 'Usuário ou email inválido'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Verifica se o script está sendo executado diretamente
if __name__ == '__main__':  
    app.run(debug=True)
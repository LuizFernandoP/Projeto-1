from flask import Flask
from configuration import configure_all
from routes.cliente import cliente_route, init_socketio
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'static/uploads/profissionais')

app.secret_key = b'\xf1\x88\xa1\xd3\xa4\xb4\x92\x1c\x1b\x8e\xfe\xe3\xd1\xd8\xab\xfe\xad\x87\x11'

configure_all(app)

app.register_blueprint(cliente_route)

# Inicialização do Socket.IO
init_socketio(app)

if __name__ == '__main__':
    # Executa a aplicação com Socket.IO
    socketio.run(app, debug=True)

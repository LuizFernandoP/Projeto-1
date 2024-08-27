from routes.home import home_route
from routes.cliente import cliente_route
from database.database import db, init_app
from database.models.cliente import Cliente

def configure_all(app):
    configure_routes(app)
    configure_db(app)

def configure_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(cliente_route, url_prefix='/clientes')

def configure_db(app):
    init_app(app)


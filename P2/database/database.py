from peewee import SqliteDatabase

db = SqliteDatabase('clientes.db')

def init_app(app):
    from database.models.cliente import Cliente  # Importação dentro da função para evitar circular imports
    with app.app_context():
        db.connect()
        db.create_tables([Cliente])

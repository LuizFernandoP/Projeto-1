from peewee import SqliteDatabase

db = SqliteDatabase('clientes.db')

def init_app(app):
    from database.models.cliente import Cliente ,Profissional  
    with app.app_context():
        db.connect()
        db.create_tables([Cliente,Profissional])
        
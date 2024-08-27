from peewee import Model, CharField
from database.database import db

class Cliente(Model):
    nome = CharField()
    email = CharField(unique=True)
    senha = CharField()

    class Meta:
        database = db
        table_name = 'clientes'

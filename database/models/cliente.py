from peewee import Model, CharField,BooleanField
from database.database import db

class Cliente(Model):
    nome = CharField()
    email = CharField(unique=True)
    senha = CharField()

    class Meta:
        database = db
        table_name = 'clientes'



class Profissional(Model):
    nome = CharField()
    especialidade = CharField()
    bio = CharField()
    foto= CharField()
    email = CharField(unique=True)
    senha = CharField()
    telefone = CharField(max_length=15)
    cep=CharField(max_length=15)
    class Meta:
        database = db
        
class Admin(Model):
    nome = CharField()
    email = CharField(unique=True)
    senha = CharField()
    is_admin = BooleanField(default=False)  

    class Meta:
        database = db
       
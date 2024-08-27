import sqlite3

#conectando...
conn = sqlite3.connect('clientes.db')
#definindo um cursor
cursor = conn.cursor()

#criando a tabela (schema)
cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes  (
        id INTEGER NOT NULL,
        nome VARCHAR NOT NULL,
        idade INTEGER  NOT NULL,
        cpf  VARCHAR(11) NOT NULL,
        email TEXT NOT NULL,
        senha    VARCHAR(11) NOT NULL,   
        fone VARCHAR(11)NOT NULL,  
        cidade TEXT,
        uf VARCHAR(2) NOT NULL,
        PRIMARY KEY (id));
""")
print('Tabela de clientes criada com sucesso.')
#desconectando...
conn.close()


conn = sqlite3.connect('profissionais.db')
cursor = conn.cursor()  
cursor.execute("""
        CREATE TABLE IF NOT EXISTS profissionais (
        id INTEGER NOT NULL,
        nome VARCHAR NOT NULL,
        idade INTEGER  NOT NULL,
        cpf  VARCHAR(11) NOT NULL,
        email TEXT NOT NULL,
        senha    VARCHAR(11) NOT NULL,   
        fone VARCHAR(11)NOT NULL,  
        cidade TEXT,
        uf VARCHAR(2) NOT NULL,
        classificação VARCHER NOT NULL,
        profissão VARCHAR NOT NULL,
        PRIMARY KEY (id));

""")

print('Tabela de profissionais criada com sucesso.')
#desconectando...
conn.close()

#tabela de acesso

conn = sqlite3.connect('acessos.cliente.db')
cursor = conn.cursor()

cursor.execute("""
        CREATE TABLE IF NOT EXISTS acesso(
        id INTEGER NOT NULL,
        username VARCHAR NOT NULL,
         data_acesso TEXT NOT NULL CHECK (LENGTH(data_acesso) = 10 AND data_acesso GLOB '[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]'),
        status TEXT NOT NULL,
        idade INTEGER  NOT NULL,
        email TEXT NOT NULL,
        senha    VARCHAR(11) NOT NULL,   
        fone VARCHAR(11)NOT NULL,  
        PRIMARY KEY (id));

""")

print('Tabela de dados atualizados com sucesso.')
#desconectando...
conn.close()

conn = sqlite3.connect('acessos.profissionais.db')
cursor = conn.cursor()

cursor.execute("""
        CREATE TABLE IF NOT EXISTS acesso(
        id INTEGER NOT NULL,
        username VARCHAR NOT NULL,
        data_acesso TEXT NOT NULL CHECK (LENGTH(data_acesso) = 10 AND data_acesso GLOB '[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]'),
        status TEXT NOT NULL,
        idade INTEGER  NOT NULL,
        email TEXT NOT NULL,
        senha    VARCHAR(11) NOT NULL,   
        fone VARCHAR(11)NOT NULL,  
        classificação VARCHER NOT NULL,
        profissão VARCHAR NOT NULL,
        PRIMARY KEY (id));         

""")


print('Tabela de dados atualizados com sucesso.')
#desconectando...
conn.close()
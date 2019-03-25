import sqlite3
#conectar
conexao=sqlite3.connect('base.db')
#Cursor para as operações
cursor=conexao.cursor()

#Criar a tabela
sql='''
CREATE TABLE clientes(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR (20) NOT NULL,
    senha VARCHAR (20) NOT NULL,
    idade INTEGER,
    cpf VARCHAR(11) NOT NULL,
    fone TEXT,
    cidade TEXT,
    uf VARCHAR(2) NOT NULL,
    criado_em DATE NOT NULL
);
'''

cursor.execute(sql)
print('Criado com sucesso')
conexao.close()
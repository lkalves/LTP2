import sqlite3
conexao=sqlite3.connect('base.db')
cursor=conexao.cursor()

sql="""
select * from clientes;
"""

cursor.execute(sql)
registros=cursor.fetchall()

for linha in registros:
    print(linha)

conexao.close()
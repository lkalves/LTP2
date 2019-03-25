import sqlite3

conexao=sqlite3.connect('base.db')
cursor=conexao.cursor()

d_id=int(input('Qual é o id da pessoa que você deseja apagar? '))

sql="""
DELETE FROM clientes
WHERE id = ?
"""
cursor.execute(sql,(d_id,))
conexao.commit()
conexao.close()
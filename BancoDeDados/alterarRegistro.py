import sqlite3
conexao=sqlite3.connect('base.db')
cursor=conexao.cursor()

a_nome=input('Qual nome você desejar trocar? ')
a_senha=input('Deseja trocar a senha? sim ou não. ')
if a_senha == 'sim':
    u_senha=input('Qual senha você desejar colocar? ')
else:
    print('Okay')
a_id=int(input('Em qual ID você deseja mudar? '))

sql="""
UPDATE clientes
SET nome = ?,
senha = ?
WHERE id= ?
"""

cursor.execute(sql,(a_nome,u_senha,a_id))
conexao.commit()
conexao.close()
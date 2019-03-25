import sqlite3

conexao=sqlite3.connect('base.db')
cursor=conexao.cursor()

while True:
    p_nome=input('Entre com o nome: ')
    p_senha=input('Entre com uma senha: ')
    p_idade=int(input('Entre com a idade: '))
    p_cpf=int(input('Entre com o CPF: '))
    p_fone=int(input('Entre com telefone: '))
    p_cidade=input('Entre com a sua cidade: ')
    p_uf=input('Entre com o seu UF: ')
    p_criado_em=input('Quando foi inscrito? Digite nesse modelo YYYY-MM-DD: ')

    # Data = 'YYYY-MM-DD'

    sql='''
    INSERT INTO clientes(nome,senha,idade,cpf,fone,cidade,uf,criado_em)
    VALUES (?,?,?,?,?,?,?,?)
    '''
    cursor.execute(sql,(p_nome,p_senha,p_idade,p_cpf,p_fone,p_cidade,p_uf,p_criado_em,))
    conexao.commit()

    continua=input('Deseja adicionar mais pessoas? ')

    if continua == 'n' or continua == 'não' or continua == 'Não':
        break

conexao.close()
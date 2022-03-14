import mysql.connector


conexao = mysql.connector(    
    host='localhost',
    user='root',
    password='root',
    database='connection_crud',
)


#CREATE
cursor = conexao.cursor()

p_cpf = 123456
p_rg = 456789
p_nome = 'Douglas alves'
script = f'INSERT INTO PESSOA(cpf,rg,nome)VALUES({p_cpf},{p_rg},"{p_nome}")'
cursor.execute(script)

conexao.commit() #commita

cursor.close()
conexao.close()

#READY
cursor = conexao.cursor()

p_cpf = 123456
p_rg = 456789
p_nome = 'Douglas alves'
script = f'SELECT * FROM PESSOA P WHERE P.CPF LIKE "%{p_cpf}%" AND P.RG LIKE "%{p_rg}%" AND P.NOME "%{p_nome}%" )'
cursor.execute(script)

resultado = cursor.fetchall()
print(resultado)

cursor.close()
conexao.close()

#UPDATE
cursor = conexao.cursor()
p_id = 1
p_cpf = 123456
p_rg = 456789
p_nome = 'Douglas alves'
script = f'UPDATE PESSOA P SET P.CPF = "{p_cpf}", P.RG = "{p_rg}", P.NOME = "{p_nome}" WHERE P.ID_PESSOA = "{p_id}")'
cursor.execute(script)

conexao.commit() #commita
cursor.close()
conexao.close()

#DELETE

cursor = conexao.cursor()
p_id = 1
p_cpf = 123456
p_rg = 456789
p_nome = 'Douglas alves'
script = f'DELETE FROM PESSOA P WHERE P.ID_PESSOA = "{p_id}" '
cursor.execute(script)

conexao.commit() #commita

cursor.close()
conexao.close()
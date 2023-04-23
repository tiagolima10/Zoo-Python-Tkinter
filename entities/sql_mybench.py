#conexao = mysql.connector.connect(host='localhost', user='root', password='', database='zoologico')

#Instalar o MySQL
#Iniciar o projeto
#Instalar o driver do MySQL (programa resposavel por realizar conexão entre python e mysql
    #pip install mysql-connector-python

#realizar conexao - inicia a conexão entre a aplicação e o banco
'''conexao = mysql.connector.connect(host='localhost', user='root', password='P@$$w0rd1304', database='atividade')'''

#criar um cursos - cria um objeto capaz de enviar orientações para o banco (para criar o cursos, é necessário já existir a conexão)
'''cursor = conexao.cursor()'''

#cursor.execute(comando) - prepara a execução de um comando sql no banco
#conexao.commit() - Realiza as ações no banco
#cursor.fetchall() - Envia os comandos de consulta do cursor ao banco e retorna a resposta (usado apenas em comandos de consulta)
#realizar um CRUD

#CREATE
'''comando = 'INSERT INTO setor (nome, faturamento) VALUES ("TI", 10000);'
cursor.execute(comando)
comando = 'INSERT INTO setor (nome, faturamento) VALUES ("Financeiro", 8000);'
cursor.execute(comando)
comando = 'INSERT INTO setor (nome, faturamento) VALUES ("Administração", 7000);'
cursor.execute(comando)
conexao.commit()'''

#READ
'''comando = 'SELECT * FROM setor;'
cursor.execute(comando)
resposta = cursor.fetchall()
print(resposta)'''

#UPDATE
'''comando = 'UPDATE setor SET faturamento = 1000 WHERE nome = "Administração";'
cursor.execute(comando)
conexao.commit()'''

#DELETE
'''comando = 'DELETE FROM setor WHERE nome="Financeiro";'
cursor.execute(comando)
conexao.commit()'''

#lembre-se de fechar a conexão e o cursos ao final da execução
'''cursor.close()
conexao.close()'''




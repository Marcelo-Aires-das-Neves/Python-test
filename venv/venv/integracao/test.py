import psycopg2

conexao = psycopg2.connect(database='postgres', 
                           user='postgres', password='admin', 
                           host='localhost', port='5432')
print(conexao.info)


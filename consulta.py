import config as bd

x = 0
emails = []

query = f'SELECT * FROM lista_email'
bd.cursor.execute(query)
resultado = bd.cursor.fetchall() # ler o banco de dados

n = len(resultado)

while x < n:
    # print(resultado[x][2])
    emails.append(resultado[x][2])

    x +=1

# print(emails)
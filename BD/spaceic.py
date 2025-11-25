import mysql.connector

# Configuração da conexão
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="jj18bb12",
    database="spaceic"
)

cursor = conexao.cursor()
cursor.execute("SELECT * FROM funcionarios")

# Buscar e exibir os resultados
resultados = cursor.fetchall()

print("=== FUNCIONÁRIOS ===")
for linha in resultados:
    print(linha)

# Efetuando alterações
conexao.commit()

# Fechar conexão
cursor.close()
conexao.close()



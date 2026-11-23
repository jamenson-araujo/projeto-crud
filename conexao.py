import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",          # Ajuste para o usuário do seu MySQL
            password="ceub123456",          # Ajuste para a senha do seu MySQL
            database="db_loja"
        )
        if conexao.is_connected():
            return conexao
    except Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")
        return None
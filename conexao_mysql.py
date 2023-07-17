import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="150119",
        database="db_estudos",
    )
    return conexao
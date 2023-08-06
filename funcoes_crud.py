from conexao_mysql import conectar
import pandas as pd

conexao = conectar()
cursor = conexao.cursor()

# Script CREATE
def criar_alunos():
    nome_aluno = input("Informe seu nome: ")
    telefone_aluno = input("Informe seu telefone (No formato 83987791174): ")
    email_aluno = input("Informe seu e-mail: ")
    sexo_aluno =  input("Informe seu sexo (M para Masculino e F para Feminino): ")
    comando = f'INSERT INTO alunos (nome, telefone, email, sexo) VALUES ("{nome_aluno}", "{telefone_aluno}", "{email_aluno}", "{sexo_aluno}")' # Comando SQL - Para VALUES de uma variavel precisa colocar o {} e, se esse valor da variavel seja string, precisa colocar "".
    
    cursor.execute(comando) # Para executar o comando/script no db.
    conexao.commit() # Caso faca CREATE, EDITE OU DELETE no db.
    print("Aluno criado com sucesso!")

# Script READ
def listar_alunos():
    comando = 'SELECT * FROM alunos' # Comando SQL - Apenas ler uma tabela.
    cursor.execute(comando) # Para executar o comando/script no db.
    resultado = cursor.fetchall() # Apenas LEITURA no db.
    
    # Converter resultado para DataFrame do pandas
    df = pd.DataFrame(resultado, columns=['id_aluno', 'nome', 'telefone', 'email', 'sexo'])
    # Imprimir tabela
    print(df)

# Script UPDATE
def atualizar_alunos():
    listar_alunos()
    id_aluno = input("Informe o ID do aluno que deseja editar: ")
    alteracao_valor = input("Qual informação você deseja atualizar (nome, telefone, email, sexo): ")
    novo_valor = input("Informe o novo valor: ")

    # Verificar a coluna escolhida e construir o comando SQL correspondente
    if alteracao_valor == "nome":
        comando = f'UPDATE alunos SET nome = "{novo_valor}" WHERE id_aluno = {id_aluno}'
    elif alteracao_valor == "telefone":
        comando = f'UPDATE alunos SET telefone = "{novo_valor}" WHERE id_aluno = {id_aluno}'
    elif alteracao_valor == "email":
        comando = f'UPDATE alunos SET email = "{novo_valor}" WHERE id_aluno = {id_aluno}'
    elif alteracao_valor == "sexo":
        comando = f'UPDATE alunos SET sexo = "{novo_valor}" WHERE id_aluno = {id_aluno}'
    else:
        print("Coluna inválida. Operação de atualização cancelada.")
        exit()

    cursor.execute(comando) # Para executar o comando/script no db.
    conexao.commit() # Para CREATE, UPDATE OU DELETE no db.
    print("ALteração realizada com sucesso!")

# Script DELETE
def deletar_alunos():
    listar_alunos()
    id_aluno = input("Informe o ID do aluno que deseja editar: ")
    comando = f'DELETE FROM alunos WHERE id_aluno = {id_aluno}' # Comando SQL - Para VALUES de uma variavel precisa colocar o {} e, se esse valor da variavel seja string, precisa colocar "".
    cursor.execute(comando) # Para executar o comando/script no db.
    conexao.commit() # Caso faca CREATE, EDITE OU DELETE no db.
    print("Aluno deletado com sucesso!")

# Sempre no final do código, para encerrar a conexão com o banco de dados
cursor.close()
conexao.close()
import sys
import pandas as pd

class Aluno:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class GerenciadorAlunos:
    def __init__(self):
        self.alunos = []

    def cadastrar_aluno(self, nome, cpf):
        aluno = Aluno(nome, cpf)
        self.alunos.append(aluno)
        print("Aluno cadastrado com sucesso!")

    def remover_aluno(self, cpf):
        for aluno in self.alunos:
            if aluno.cpf == cpf:
                self.alunos.remove(aluno)
                print("Aluno removido com sucesso!")
                return
        print("Aluno não encontrado!")

    def editar_aluno(self, cpf, novo_nome):
        for aluno in self.alunos:
            if aluno.cpf == cpf:
                aluno.nome = novo_nome
                print("Dados do aluno atualizados com sucesso!")
                return
        print("Aluno não encontrado!")

    def listar_alunos(self):
        print("Lista de alunos:")
        for aluno in self.alunos:
            print(f"Nome: {aluno.nome}, CPF: {aluno.cpf}")

def exibir_menu():
    print("Escolha uma opção:")
    print("1 - Cadastrar Aluno")
    print("2 - Remover Aluno")
    print("3 - Editar Aluno")
    print("4 - Listar Alunos")
    print("5 - Sair")

gerenciador = GerenciadorAlunos()

def cadastrar_aluno():
    print("Opção selecionada: Cadastrar Aluno")
    nome = input("Digite o nome do aluno: ")
    cpf = input("Digite o CPF do aluno: ")
    gerenciador.cadastrar_aluno(nome, cpf)

def remover_aluno():
    print("Opção selecionada: Remover Aluno")
    cpf = input("Digite o CPF do aluno que deseja remover: ")
    gerenciador.remover_aluno(cpf)

def editar_aluno():
    print("Opção selecionada: Editar Aluno")
    cpf = input("Digite o CPF do aluno que deseja editar: ")
    novo_nome = input("Digite o novo nome do aluno: ")
    gerenciador.editar_aluno(cpf, novo_nome)

def listar_alunos():
    print("Opção selecionada: Listar Alunos")
    gerenciador.listar_alunos()

def sair_menu():
    sys.exit()

# Exemplo de uso do menu
while True:
    exibir_menu()
    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        cadastrar_aluno()
    elif opcao == "2":
        remover_aluno()
    elif opcao == "3":
        editar_aluno()
    elif opcao == "4":
        listar_alunos()
    elif opcao == "5":
        sair_menu()
    else:
        print("Opção inválida. Digite novamente.")
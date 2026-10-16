from services.aluno_service import AlunoService
from services.treino_service import TreinoService
from services.exercicio_service import ExercicioService

from repositories.aluno_repository import AlunoRepository
from repositories.treino_repository import TreinoRepository
from repositories.exercicio_repository import ExercicioRepository

repositoryAluno = AlunoRepository()
repositoryTreino = TreinoRepository()
repositoryExercicio = ExercicioRepository()

aluno_service = AlunoService(repositoryAluno)
treino_service = TreinoService(repositoryTreino)
exercicio_service = ExercicioService(repositoryExercicio)

#================================-MODELO-API-====================================================
from fastapi import FastAPI, HTTPException
from routes.aluno_routes import router as aluno_router
from routes.treino_routes import router as treino_router
from routes.exercicio_routes import router as exercicio_router

app = FastAPI(title="sistema gerenciador de alunos de academia", version="0.2.0")

app.include_router(aluno_router)
app.include_router(treino_router)
app.include_router(exercicio_router)




#================================-MODELO-TERMINAL-====================================================
def limpar_tela():
    print("\n" * 3)

def pausa():
    input("\nPressione ENTER para continuar...")

def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite apenas um número inteiro.")

def mostrar_resultado(resultado):
    if resultado is None:
        print("\nNenhum resultado encontrado.")

    elif isinstance(resultado, list):
        if len(resultado) == 0:
            print("\nNenhum resultado encontrado.")
        else:
            for item in resultado:
                print(item)

    else:
        print(resultado)

def gerenciar_alunos():

    while True:

        limpar_tela()

        print("=======================================")
        print("          GERENCIAR ALUNOS")
        print("=======================================")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Atualizar aluno")
        print("4 - Deletar aluno")
        print("5 - Desativar aluno")
        print("6 - Ativar aluno")
        print("7 - Buscar aluno por ID")
        print("8 - Buscar alunos por plano")
        print("0 - Voltar")
        print("=======================================")

        opcao = input("Escolha uma opção: ").strip()

        match opcao:

            case "1":
                limpar_tela()

                print("========== CADASTRAR ALUNO ==========")

                nome = input("Nome: ").strip()
                idade = ler_inteiro("Idade: ")
                plano = input(
                    "Plano (basico/intermediario/pro): "
                ).strip().lower()

                resultado = aluno_service.cadastrar(
                    nome,
                    idade,
                    plano
                )

                print("\nAluno cadastrado com sucesso!")
                mostrar_resultado(resultado)

                pausa()

            case "2":
                limpar_tela()

                print("========== LISTAR ALUNOS ==========")

                resultado = aluno_service.listar()

                mostrar_resultado(resultado)

                pausa()

            case "3":
                limpar_tela()

                print("========== ATUALIZAR ALUNO ==========")

                id = ler_inteiro("ID do aluno: ")
                idade = ler_inteiro("Nova idade: ")

                plano = input(
                    "Novo plano (basico/intermediario/pro): "
                ).strip().lower()

                resultado = aluno_service.atualizar(
                    id,
                    idade,
                    plano
                )

                print("\nAluno atualizado com sucesso!")
                mostrar_resultado(resultado)

                pausa()

            case "4":
                limpar_tela()

                print("========== DELETAR ALUNO ==========")

                id = ler_inteiro("ID do aluno: ")

                resultado = aluno_service.deletar(id)

                print("\nAluno deletado com sucesso!")
                mostrar_resultado(resultado)

                pausa()

            case "5":
                limpar_tela()

                print("========== DESATIVAR ALUNO ==========")

                id = ler_inteiro("ID do aluno: ")

                resultado = aluno_service.desativar(id)

                print("\nAluno desativado com sucesso!")
                mostrar_resultado(resultado)

                pausa()

            case "6":
                limpar_tela()

                print("========== ATIVAR ALUNO ==========")

                id = ler_inteiro("ID do aluno: ")

                resultado = aluno_service.ativar(id)

                print("\nAluno ativado com sucesso!")
                mostrar_resultado(resultado)

                pausa()

            case "7":
                limpar_tela()

                print("========== BUSCAR ALUNO ==========")

                id = ler_inteiro("ID do aluno: ")

                resultado = aluno_service.buscar_por_id(id)

                mostrar_resultado(resultado)

                pausa()

            case "8":
                limpar_tela()

                print("========== BUSCAR POR PLANO ==========")

                plano = input("Plano: ").strip().lower()

                resultado = aluno_service.buscar_por_plano(plano)

                mostrar_resultado(resultado)

                pausa()

            case "0":
                return

            case _:
                print("\nOpção inválida.")
                pausa()

def gerenciar_treinos():

    while True:

        limpar_tela()

        print("=======================================")
        print("          GERENCIAR TREINOS")
        print("=======================================")
        print("1 - Cadastrar treino")
        print("2 - Buscar treino por ID")
        print("3 - Atualizar treino")
        print("4 - Deletar treino")
        print("0 - Voltar")
        print("=======================================")

        opcao = input("Escolha uma opção: ").strip()

        match opcao:

            case "1":
                limpar_tela()

                print("========== CADASTRAR TREINO ==========")

                nome = input("Nome do treino: ").strip()

                dia_semana = input(
                    "Dia da semana: "
                ).strip().lower()

                id_aluno = ler_inteiro("ID do aluno: ")

                resultado = treino_service.cadastrar_treino(
                    nome,
                    dia_semana,
                    id_aluno
                )

                print("\nTreino cadastrado com sucesso!")
                mostrar_resultado(resultado)

                pausa()

            case "2":
                limpar_tela()

                print("========== BUSCAR TREINO ==========")

                id = ler_inteiro("ID do treino: ")

                resultado = treino_service.buscar_por_id(id)

                mostrar_resultado(resultado)

                pausa()

            case "3":
                limpar_tela()

                print("========== ATUALIZAR TREINO ==========")

                dia_semana = input(
                    "Novo dia da semana: "
                ).strip().lower()

                nome = input(
                    "Novo nome do treino: "
                ).strip()

                id_aluno = ler_inteiro("ID do aluno: ")

                resultado = treino_service.atualizar(
                    dia_semana,
                    nome,
                    id_aluno
                )

                print("\nTreino atualizado com sucesso!")
                mostrar_resultado(resultado)

                pausa()

            case "4":
                limpar_tela()

                print("========== DELETAR TREINO ==========")

                dia_semana = input(
                    "Dia da semana: "
                ).strip().lower()

                id_aluno = ler_inteiro("ID do aluno: ")

                resultado = treino_service.deletar(
                    dia_semana,
                    id_aluno
                )

                print("\nTreino deletado com sucesso!")
                mostrar_resultado(resultado)

                pausa()

            case "0":
                return

            case _:
                print("\nOpção inválida.")
                pausa()

def gerenciar_exercicios():

    while True:

        limpar_tela()

        print("=======================================")
        print("        GERENCIAR EXERCÍCIOS")
        print("=======================================")
        print("1 - Cadastrar exercício")
        print("2 - Buscar exercícios por treino")
        print("3 - Atualizar exercício")
        print("4 - Deletar exercício")
        print("0 - Voltar")
        print("=======================================")

        opcao = input("Escolha uma opção: ").strip()

        match opcao:

            case "1":
                limpar_tela()

                print("======= CADASTRAR EXERCÍCIO =======")

                nome = input(
                    "Nome do exercício: "
                ).strip()

                series = ler_inteiro("Séries: ")
                repeticoes = ler_inteiro("Repetições: ")
                id_treino = ler_inteiro("ID do treino: ")

                resultado = exercicio_service.cadastrar_treino(
                    nome,
                    series,
                    repeticoes,
                    id_treino
                )

                print("\nExercício cadastrado com sucesso!")
                mostrar_resultado(resultado)

                pausa()

            case "2":
                limpar_tela()

                print("======= BUSCAR EXERCÍCIOS =======")

                id_treino = ler_inteiro(
                    "ID do treino: "
                )

                resultado = exercicio_service.buscar_por_id(
                    id_treino
                )

                mostrar_resultado(resultado)

                pausa()

            case "3":
                limpar_tela()

                print("======= ATUALIZAR EXERCÍCIO =======")

                nome = input(
                    "Novo nome: "
                ).strip()

                series = ler_inteiro(
                    "Novas séries: "
                )

                repeticoes = ler_inteiro(
                    "Novas repetições: "
                )

                id = ler_inteiro(
                    "ID do exercício: "
                )

                resultado = exercicio_service.atualizar(
                    nome,
                    series,
                    repeticoes,
                    id
                )

                print("\nExercício atualizado com sucesso!")
                mostrar_resultado(resultado)

                pausa()

            case "4":
                limpar_tela()

                print("======= DELETAR EXERCÍCIO =======")

                id = ler_inteiro(
                    "ID do exercício: "
                )

                resultado = exercicio_service.deletar(id)

                print("\nExercício deletado com sucesso!")
                mostrar_resultado(resultado)

                pausa()

            case "0":
                return

            case _:
                print("\nOpção inválida.")
                pausa()

def menu_principal():

    while True:

        limpar_tela()

        print("=======================================")
        print("          SISTEMA DE ACADEMIA")
        print("=======================================")
        print("1 - Gerenciar alunos")
        print("2 - Gerenciar treinos")
        print("3 - Gerenciar exercícios")
        print("0 - Sair")
        print("=======================================")

        opcao = input("Escolha uma opção: ").strip()

        match opcao:

            case "1":
                gerenciar_alunos()

            case "2":
                gerenciar_treinos()

            case "3":
                gerenciar_exercicios()

            case "0":
                limpar_tela()

                print("Programa encerrado.")

                break

            case _:
                print("\nOpção inválida.")
                pausa()

if __name__ == "__main__":
    menu_principal()
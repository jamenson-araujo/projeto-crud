from conexao import conectar
from operacoes.inserir import inserir
from operacoes.consultar import consultar
from operacoes.alterar import alterar
from operacoes.excluir import excluir

def menu():
    conexao = conectar()
    if not conexao:
        print("Não foi possível iniciar o sistema sem conexão com o banco.")
        return

    try:
        while True:
            print("\n==============================")
            print("   SISTEMA CRUD - PRODUTOS    ")
            print("==============================")
            print("1 - Inserir Produto (Create)")
            print("2 - Consultar Produtos (Read)")
            print("3 - Alterar Produto (Update)")
            print("4 - Excluir Produto (Delete)")
            print("0 - Sair")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                inserir(conexao)
            elif opcao == "2":
                consultar(conexao)
            elif opcao == "3":
                alterar(conexao)
            elif opcao == "4":
                excluir(conexao)
            elif opcao == "0":
                print("Encerrando o sistema...")
                break
            else:
                print("Opção inválida! Tente novamente.")
    finally:
        if conexao.is_connected():
            conexao.close()
            print("Conexão com o MySQL encerrada com segurança.")

if __name__ == "__main__":
    menu()
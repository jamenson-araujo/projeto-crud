from mysql.connector import Error

def consultar(conexao):
    print("\n--- CONSULTAR PRODUTOS ---")
    print("1 - Listar todos os produtos")
    print("2 - Buscar produto por código")
    opcao = input("Escolha uma opção: ").strip()

    try:
        cursor = conexao.cursor()

        if opcao == "1":
            sql = "SELECT Cd_Produto, Nome_Produto FROM Tb_produto ORDER BY Cd_Produto"
            cursor.execute(sql)
            resultados = cursor.fetchall()

            if not resultados:
                print("Nenhum produto cadastrado.")
            else:
                print("\nCódigo | Nome do Produto")
                print("-" * 30)
                for codigo, nome in resultados:
                    print(f"{codigo:<6} | {nome}")

        elif opcao == "2":
            codigo = int(input("Digite o código do produto: "))
            sql = "SELECT Cd_Produto, Nome_Produto FROM Tb_produto WHERE Cd_Produto = %s"
            cursor.execute(sql, (codigo,))
            produto = cursor.fetchone()

            if produto:
                print(f"\nEncontrado -> Código: {produto[0]} | Nome: {produto[1]}")
            else:
                print(f"Nenhum produto encontrado com o código {codigo}.")
        else:
            print("Opção de consulta inválida.")

    except ValueError:
        print("Erro: Digite um código numérico válido.")
    except Error as erro:
        print(f"Erro no banco ao consultar: {erro}")
    finally:
        if "cursor" in locals():
            cursor.close()
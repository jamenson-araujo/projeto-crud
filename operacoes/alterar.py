from mysql.connector import Error

def alterar(conexao):
    print("\n--- ALTERAR PRODUTO ---")
    try:
        codigo = int(input("Código do produto que deseja alterar: "))
        novo_nome = input("Novo nome do produto: ").strip()

        if not novo_nome:
            print("Aviso: O novo nome não pode ficar vazio.")
            return

        cursor = conexao.cursor()
        # A cláusula WHERE garante que apenas o registro escolhido seja alterado
        sql = "UPDATE Tb_produto SET Nome_Produto = %s WHERE Cd_Produto = %s"
        cursor.execute(sql, (novo_nome, codigo))
        conexao.commit()

        # rowcount verifica se alguma linha realmente foi afetada no banco
        if cursor.rowcount > 0:
            print(f"Sucesso! Produto {codigo} atualizado para '{novo_nome}'.")
        else:
            print(f"Nenhum produto encontrado com o código {codigo}.")

    except ValueError:
        print("Erro: O código deve ser um número inteiro.")
    except Error as erro:
        print(f"Erro no banco ao alterar: {erro}")
    finally:
        if "cursor" in locals():
            cursor.close()
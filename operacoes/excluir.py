from mysql.connector import Error

def excluir(conexao):
    print("\n--- EXCLUIR PRODUTO ---")
    try:
        codigo = int(input("Código do produto que deseja excluir: "))
        confirmacao = input(f"Confirmar exclusão do produto {codigo}? (S/N): ").strip().upper()

        if confirmacao != "S":
            print("Exclusão cancelada.")
            return

        cursor = conexao.cursor()
        # A cláusula WHERE impede que todos os dados da tabela sejam apagados
        sql = "DELETE FROM Tb_produto WHERE Cd_Produto = %s"
        cursor.execute(sql, (codigo,))
        conexao.commit()

        if cursor.rowcount > 0:
            print(f"Sucesso! Produto {codigo} removido do banco.")
        else:
            print(f"Nenhum produto encontrado com o código {codigo}.")

    except ValueError:
        print("Erro: O código deve ser um número inteiro.")
    except Error as erro:
        print(f"Erro no banco ao excluir: {erro}")
    finally:
        if "cursor" in locals():
            cursor.close()
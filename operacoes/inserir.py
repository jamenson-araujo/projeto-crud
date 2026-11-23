from mysql.connector import Error

def inserir(conexao):
    print("\n--- CADASTRAR PRODUTO ---")
    try:
        nome = input("Nome do Produto: ").strip()

        if not nome:
            print("Aviso: O nome do produto não pode ficar vazio.")
            return

        cursor = conexao.cursor()
        # Omitimos Cd_Produto pois o MySQL preencherá via AUTO_INCREMENT
        sql = "INSERT INTO Tb_produto (Nome_Produto) VALUES (%s)"
        
        # A vírgula em (nome,) é obrigatória para o Python entender como tupla
        cursor.execute(sql, (nome,))
        conexao.commit()

        # lastrowid captura o ID gerado automaticamente pelo banco
        codigo_gerado = cursor.lastrowid
        print(f"Sucesso! Produto '{nome}' cadastrado com o código {codigo_gerado}.")

    except Error as erro:
        print(f"Erro no banco ao inserir: {erro}")
    finally:
        if "cursor" in locals():
            cursor.close()
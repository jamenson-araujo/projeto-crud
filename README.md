# Sistema CRUD de Produtos (Python + MySQL)

Aplicação desenvolvida para gerenciamento de produtos (`Tb_produto`) utilizando Python puro e SQL nativo via `mysql-connector-python`.

## Estrutura do Projeto
- `sql/banco.sql`: Script de criação do banco `db_loja` e da tabela `Tb_produto`.
- `conexao.py`: Configuração de conexão com o servidor MySQL.
- `operacoes/`: Módulos isolados para `inserir.py`, `consultar.py`, `alterar.py` e `excluir.py`.
- `main.py`: Menu principal e controle de fluxo.

## Como Executar
1. Execute o script `sql/banco.sql` no seu MySQL Server.
2. Configure o usuário e senha do seu banco no arquivo `conexao.py`.
3. Instale a dependência:
   ```bash
   pip install -r requirements.txt





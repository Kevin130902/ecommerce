import pandas as pd
import sqlite3

class Ecommerce:
    def __init__ (self, db='db.sqlite3'):
        self.conn = sqlite3.connect(db)
        self.menu()

    def menu(self):
        while True:
            print('\n'
                '[1]-Create\n'
                '[2]-Read\n'
                '[3]-Update\n'
                '[4]-Delete\n'
                '[5]-Exit\n\n'
                )
            op = int(input('Escolha uma opção: '))
            match op:
                case 1:
                    self.menu_create()
                case 2:
                    print('Read')
                case 3:
                    print('Update')
                case 4:
                    print('Delete')
                case 5:
                    break
                case _:
                    print('Opção inválida.')

    def create(self, valores):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO api_produto (tituloProduto, preco, descricao, imagemProduto,
               categoriaProduto, classProduto, exibirHome)
            VALUES(?,?,?,?,?,?,?)""",
            valores,
        )
        self.conn.commit()
        print('Produto cadastrado com sucesso!!!')

    def menu_create(self):
        print(
            '\n'
            '[1]-Título\n'
            '[2]-Preço\n'
            '[3]-Descrição\n'
            '[4]-Imagem\n'
            '[5]-Categoria\n'
            '[6]-Classificação\n'
            '[7]-Exibir\n'
        )
        titulo = input("Título: ")
        preco = float(input('Preço: '))
        descricao = input("Descrição: ")
        imagemProduto = input("Imagem: ")
        categoriaProduto = input("Categoria: ")
        classProduto = input("Classificação: ")
        exibirHome = input("Exibir(True, False): ")

        self.create((titulo, preco, descricao, imagemProduto,
               categoriaProduto, classProduto, exibirHome))

    def read(self):
        print(
            "\n"
            "[1]-Listar todos os produtos\n"
            "[2]-Listar por ID"
        )

        op = int(input("Escolha a opção: "))

        match op:
            case 1:
                df = pd.read_sql_query("SELECT * FROM api_produto")
            case 2:
                valor = int(input("ID: "))
                query = f"SELECT * FROM api_produto WHERE id = {valor}"
                df = pd.read_sql_query(query, self.conn)

                print(df)
                return
            case _:
                print("Escolhe uma opção válida...")

    def update(self, id, data):
        (titulo, preco, descricao, imagemProduto, categoriaProduto, classProduto, exibirHome) = data

        cursor = self.conn.cursor()
        campos = []
        valores = []

        for v in data:
            valores.append(v)

        if titulo:
            campos.append("tituloProduto = ?")

        if preco:
            campos.append("preco = ?")

        if descricao:
            campos.append("descricao = ?")

        if imagemProduto:
            campos.append("imagemProduto = ?")

        if categoriaProduto:
            campos.append("categoriaProduto = ?")

        if classProduto:
            campos.append("classProduto = ?")

        if exibirHome:
            campos.append("exibirHome = ?")

        valores.append(id)
        cursor.execute(f"UPDATE api_produto SET {", ".join(campos)} WHERE id")


ecommerce = Ecommerce()
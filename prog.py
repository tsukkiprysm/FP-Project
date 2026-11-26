# GRUPO: P16G

# Desenvolvam o trabalho neste ficheiro.
# Podem criar outros ficheiros e importá-los aqui.


# Ler a base de dados
def read_database(database_file):
    product_dict = {}
    with open(database_file, "r") as database:
        next(database)
        for product_info in database:
            product_info = product_info.strip()
            code, name, category, price, stock, receipt = product_info.split(";")
            product_dict[code] = {
                "name": name,
                "category": category,
                "price": float(price),
                "stock": int(stock),
                "receipt": receipt == "S",
            }
    return product_dict

#Consultar produtos disponíveis


#Adicionar produtos ao carrinho


#Consultar o carrinho de compras


#Aplicar comparticipações por categoria


#Pagar e emitir fatura


#Terminar e guardar o stock


#Interface

def main():
    database = "produtos.txt"
    product_list = read_database(database)
    print(product_list)


if __name__ == "__main__":
    main()


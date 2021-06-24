import e_commerce

# Instancias
item01 = e_commerce.Item('Camiseta Corinthians', preco=159)
item02 = e_commerce.Item('Camisa Xadrez', preco=99)
item03 = e_commerce.Item('Caneca Bob Esponja', preco=199)
cliente01 = e_commerce.Cliente()

cliente01.adiciona_item(item01)
cliente01.adiciona_item(item02)
cliente01.adiciona_item(item03)

print(cliente01.consolidar_compra())

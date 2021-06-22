produtos = []
def verProduto(nome, tamanho, preco):
    produto = {
        'nome': nome,
        'tamanho': tamanho,
        'preco': preco
    }
    produtos.append(produto)

def addProduto():
    for p in produtos:
        print('=======')
        print(f"Nome:{p['nome']}")
        print(f"tamanho: {p['tamanho']}")
        print(f"preco: {p['preco']}")

def removerProduto(produto):
    for p in produtos:
        if p ['nome'] == produto:
            produtos.remove(p)
addProduto()
verProduto()


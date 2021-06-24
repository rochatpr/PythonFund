class Item():
    # Metodo construtor
    def __init__(self, nome, descricao='', preco=0):
        self.item = {
        "nome":nome,
        "descricao":descricao,
        "preco":preco
        }
    #Metodo de acesso
    def get_nome(self):
        return self.__nome
    
    def get_desc(self):
        return self.__descricao
    
    def get_preco(self):
        return self.__preco
    
    #Metodo de definicao
    def set_nome(self, nome):
        self.__nome = nome
    
    def set_preco(self, preco):
        self.__preco = preco

    def set_desc(self, descricao):
        self.__descricao = descricao
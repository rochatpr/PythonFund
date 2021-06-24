# Orientação a objeto

# Paradigma de programação - Resolve um tipo de problema

# Escrevemos codigos até agora usando o paradigma procedural e funcional

# Problemas que o paradigma orientado a objetos resolve:

# - Reutilização do código
# - Centralização dos dados
# - Aumento do tamanho

# Através do paradigma POO, temos:

#Capacidade de manipular os dados de forma a respeitar as regras de negocio
#Restringir o acesso aos dados

# Conceitos:

# abstração - Isolar a nossa logica, mantendo o usuário sem a necessidade de compreender
# Encapsulamento - Isolar seus atributos do cliente (__atributo).
# Herança - herdar atributos e métodos de outro objeto.
# Polimorfismo - mesmo herdando caracteristicas, eu posso alterar essas caracteristica no objeto que herdou sem afetar o objeto inicial.

# class Casa01():

#     quartos = 2
#     sala = 1
#     banheiro = 2
#     garagem = 2
#     cozinha = 'Americana'

#     def informacoes(self):
#         print(self.quartos)
#         print(self.garagem)
#         print(self.cozinha)
#         print(self.banheiro)
#         print(self.sala)

# casaPedro = Casa01
# casaPedro

# class automovel():
#     def __init__(self):
#         print()
#         self.motor = True
#         self.rodas = 4
#         self.portas = 2

#     def ligar(self):
#         pass

#     def desligar(self):

#     def acelerar(self):
#         pass

#     def frear(self):
#         pass

# hb20 = automovel()

# class contaCorrente():
#     def __init__(self):
#         self.__nomeCliente = input('Nome de cliente: ')
#         self.__idBanco = 777
#         self.__idAgencia = int(input('Digite o número da agencia: '))
#         self.__saldo = 0
        
#     def extrato(self):
#         print('------Extrato-----')
#         print(f'Nome: {self.__nomeCliente}')
#         print(f'Saldo: {self.__saldo}')

#     def sacar(self, valor):
#         if self.__saldo >= valor:
#             print(f'Saldo anterior: {self.__saldo}')
#             self.__saldo -= valor
#             print(f'Novo saldo: {self.__saldo}')
#         else:
#             print('Saldo Insuficiente')

    

#     def depositar(self, valor):
#         print(f'Saldo anterior: {self.saldo}')
#         self.saldo += valor
#         print(f'Novo saldo: {self.saldo}')
        
# Herança

class Pai():
    def __init__(self):
        self.nome = 'Joao'
        self.sobrenome = 'Pereira Pinto'
        self.profissao = 'Marceneiro'

    def trabalhar(self):
        print(f'Trabalhando como {self.profissao}')

class Filho(Pai):
    def __init__(self):
        Pai().__init__()
# class Colaborador():

#     def __init__(self):
#         self.__nome = input('Nome: ')
#         self.__matricula = input('Matricula: ')
#         self.__endereco = input('Endereço: ')
#         self.__dataNascimento = input('Data de nascimento: ')
#         self.__salario = int(input('Salario: '))
    
#     def funcao(self):
#         self.__funcao = 'N1'
#         print(f'Trabalhando {self.__funcao}')

# class ColaboradorN2(Colaborador):

#     def __init__(self):
#         Colaborador().__init__()

        


# Palavras-chaves:

# Objeto - Instacia de classe
# Classe - Definição de como o objeto deve ser
# Método construtor - Método que inicializa atributos na criação do obj
# Instância - uma variavel que contém a classe
# Atributo - Caracteristica
# Método - ações
# self - Referencia ao objeto
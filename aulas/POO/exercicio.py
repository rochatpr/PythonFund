# Crie uma Classe Colaborador que tenha atributos e métodos
# Crie uma Classe Gerente que herde de Colaborador e altere funcao, salario
# Crie uma Classe suporteN1 que herde de Colaborador e altere funcao e salario

class Colaborador():
    def __init__(self):
        self.nome = input('Nome: ')
        self.idade = input('Idade: ')
        self.funcao = 'SysAdmin'
        self.salario = 2000

class Gerente(Colaborador):
    def __init__(self):
        super().__init__()

class suporteN1(Colaborador):
    def __init__(self):
        super().__init__()

joao = Gerente()
joao.salario
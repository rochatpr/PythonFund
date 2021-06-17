#Regras da linguagem
#Palavras reservadas não podem ser utilizadas para nomear outras coisas
#Estruturas de Condições, repetições, funções, classes e contextos sempre terminaç com dois pontos
#comandos que estão dentro de estruturas são identadas com 4 espaços
#Objetos criados não podem começar com numeros, virgula, ponto...

#Estrutura de repetição

##While
contador = 0
while contador < 100:
    print(contador)
    contador += 1

while True:

    print('Sistema integrado de escolha')
    print('Digite:')
    print('1 - Para Escolher primeira opção')
    print('2 - Para Escolher a segunda opção')
    print('0 - Para Sair')
    opcao = int(input('>>>'))
    if opcao == 1:
        print('Você escolheu a primeira opção')
    elif opcao == 2:
        print('Você escolher a segunda opção')
    elif opcao == 0:
        break
    else:
        print('Opção Inválida')
##For

# texto = 'Olá eu sou um texto'

# for caracter in texto:
#     print(f"Agora a variavel caracter é {caracter}")

produtos = ['Camiseta A','Camiseta B','Camiseta C','Calça 1','Calça 2']

for prod in produtos:
    print()

#Conjuntos - Coleções

#Listas - Conjunto de objetos
lista = ["String 1 ", "String 2", 2, 5, 1.6, True]

#Metodo de lista
lista.append('Arquivo 1')
lista.insert(2,'Dado')
lista.remove('Dado')
lista.pop(1)
lista.sort('Dado')
lista.clear()

#Tuplas - Lista não alteravel

#cadastro = (Joao','Nascimento',26)
#cadastro.count()
#cadastro.index()

#Dicionario
dados_pessoais = {"nome":"João",
                  "idade": 36,
                  "Telefone":"119999999",
                  "E-mail":"joao@teste.com"}

dados_estaduais = {
    "SP":{
        "Nome":"Sao Paulo",
        "Populacao": 15000000,
        "IDH": 15
    },
    "BH":{
    "Nome": "Belo Horizonte",
    "Populacao": 100000,
    "IDH": 12
    },
    "RJ":{
    "Nome": "Rio de Janeiro",
    "Populacao":1300000,
    "IDH":9 
    },
}

#Metodos de dict

dados_pessoais.keys()
dados_pessoais.values()
dados_pessoais.get()
dados_pessoais.clear()

#Sets - Conjunto de valores únicos

#conjunto = 

# n1=5
# n2=10

# if n1 > n2:

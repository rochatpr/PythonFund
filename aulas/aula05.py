# As 4 maneiras de trabalhar com funções

# 1 - Utilizando as funções built-in

#print()
#input()

#2 - Importando apartir de modulos

#import os 
#os.system('ls -la')

#3 - Criando suas proprias funções

# def soma(x,y):
#     return x + y

#4 - Utilizando funções anonimas

# soma = lambda x, y: x + y

#Escopo


#Parametros não obrigatórios

# def multiplica(x,y,desconto=1):
#     total = total * desconto

# def soma(x=1, y=1):
#     print

# print(multiplica(10, 15))

#Paramentro com palavra-chave

#Multiplos argumentos

#Args
# def soma (*num):
#     total = 0
#     for i in num:
#         total += i
#     print(total)

#Multiplos argumentos com palavras-chave

#kwargs
# def checkout(**valores):
#     total = 0
#     for valor in valores.values:
#         print(valor)

# accounts
# [{'nome':'João','verba': 1000, 'restante': 500}, {'nome': 'Carlos','verba':1000, 'restante':0}]
# sem_verba = list(map(lambda x: x['restante']))

# from functools import reduce

# soma = reduce((lambda x , y: x + y), lista)
# menor = reduce((lambda x, y: x if(x < y) else y), lista)
# par = list(filter(lambda x: x % 2 == 0, lista))

def soma(x=1, y=1):
    print(x + y)


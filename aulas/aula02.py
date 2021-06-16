# Strings - Conjunto de caracteres

nome = input("Qual é o seu nome")

texto = "Olá {}, seja bem vindo".format(nome)

dividindoTexto = texto.split('a')
caixaBaixa = texto.lower()
caixaAlta = texto.upper()
texto.endswith("!")
texto.startswith('Olá')
texto.strip('a')

###print(caixaAlta)

#Indexação de String

texto2 = "Apenas uma String"
print(texto2[:6])
print(texto2[6:])
print(texto2[5:10])
print(texto2[:]) 
print(texto2[::])
print(texto2[::2])

# Estrutura Condicional

nome = input('Digite seu nome:')
idade = int(input('Digite sua idade:'))
habilitacao = input('Possui habilitacao? (S/N)')
credito = True

if idade >= 18 and habilitacao == 's' and credito == True:
    print(f'Bem vindo(a) {nome}')
    print('Voce pode alugar um carro!')

else:
    print(f'Bem vindo(a) {nome} infelizmente você não pode alugar um carro')
  
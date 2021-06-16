#Criar uma aplicação de Calculo de média
nome = input('Digite seu nome')
n1 = float (input ('Digite a primeira nota:'))
n2 = float (input ('Digite a segunda  nota:'))
n3 = float (input ('Digite a terceira nota:'))
n4 = float (input ('Digite a quarta nota:'))

media = (n1 + n2 + n3 + n4) / 4
if media >= 7:
    print(f'Olá{nome} você foi Aprovado!')
    print('Sua média é :',(media))
elif media >= 6: 
    print(f'Olá{nome} está de Recuperação!')
    print(f'Sua média é {media}:')
else:
    print(f'Olá{nome} Você está reprovado!')
    print(f'Sua média é {media}:')
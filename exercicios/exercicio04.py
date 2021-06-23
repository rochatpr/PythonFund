# Criar uma aplicação que consuma a api do viacep

#Funções:
    # informaRua - recebe um cep e informa a rua 
    # informaBairro - recebe um cep e informa o bairro

    #Consultar CEP Full - recebe o cep e informa o endereço completo

import json
import requests

def main():
    while True:
        infCep = input('Informe um CEP: ')
        consulta = consultaCEP(infCep)
        print('Menu de Consulta de CEP')
        print('1 - Consultar endereço completo')
        print('2 - Consultar nome da rua')
        print('3 - Consultar nome do bairro')
        opcao = input('>>>> ')
        if opcao == '1':
            print(consulta)
        elif opcao == '2':
            print(consulta['logradouro'])
        elif opcao == '3':
            print(consulta['bairro'])
        elif opcao == '4':
            break
        else:
            print('Opção invalida')
    
        

def consultaCEP(cep):
    viacep = f'https://viacep.com.br/ws/{cep}/json'
    req = requests.get(viacep).text
    # conteudo = json.loads(req.content)
    return req

main()





# RAM

# volatil

# ROM

# não volatil

# Abrindo arquivo em modo de leitura
# arquivo = open('texto.txt', 'r')

#Abrir arquivo em modo de escrita
# arquivo = open('texto.txt', 'w')

#Abrir arquivo em modo de criação
# arquivo = open('texto.txt','x')

#Abrir arquivo em modo de adição
# arquivo = open('texto.txt','a')
# arquivo.write('Alguma coisa')
# arquivo.close()

#Modo de atualização (leitura e escrita)
# arquivo = open('texto.txt','r+')
# print(arquivo.read())
# arquivo.write('teste 03')
# print(arquivo.read())
# arquivo.close()

#Contextos

# with open('texto.txt','r+') as arquivo:
#     nome = input('Digite um nome:')
#     arquivo.write(nome)
#     arquivo.read()

def main():
    dic_opcoes = {
        '1': 'consultar',
        '2': 'inserir',
        '3': 'deletar',
        '4': 'atualizar',
        '5': 'exit'
    }

    while True:
        print('Digite a opcao desejada')
        print('1 - consultar')
        print('2 - inserir')
        print('3 - deletar')
        print('4 - atualizar')
        print('5 - sair')
        opcao = input ('>>>>> ')

        if opcao in '12345':
            dic_opcoes[opcao]()
        else:
            print('Opcao invalida')

def consultar():
    cpf = input('Informe o CPF: ')

    with open('registro.txt','r') as arquivo:
        conteudo = arquivo.readlines()
        for linha in conteudo:
            if cpf in linha.split('\t'):
                registro = linha.split('\t')
                print('CPF', registro[0])
                print('Nome', registro[1])
                print('Idade', registro[2])
                print('Sexo', registro[3])
                print('Nacionalidade', registro[4])
            else:
                print('Registro não encontrado')

def inserir():
    cpf = input('CPF: ')
    nome = input('Nome: ')
    idade = input('Idade: ')
    sexo = input('Sexo: ')
    nacionalidade = input('Nacionalidade: ')

    registro = f'{cpf}\t{nome}\t{idade}\t{sexo}\t{nacionalidade}\n'

    with open ('registro.txt', 'a+') as arquivo:
        arquivo.write(registro)

def deletar():
    cpf = input('Informe o CPF: ')

    with open('registro.txt','r') as arquivo:
        conteudo = arquivo.readlines()
    for linha in range(0, len(conteudo)):
        if cpf in conteudo[linha].split('\t'):
            registro = linha.split('\t')
            print('CPF', registro[0])
            print('Nome', registro[1])
            print('Idade', registro[2])
            print('Sexo', registro[3])
            print('Nacionalidade', registro[4])
        if input('Deseja excluir o registro? (S/N)').upper() == 'S':
            conteudo.pop(linha)
            with open('registro.txt', 'w') as arquivo:
                arquivo.write(''.join(conteudo))
            break
        else:
            print('Cancelado pelo usuario')
    else:
        print('Registro não encontrado')
main()

def atualizar():
    cpf = input('Informe o CPF: ')
    with open('registro.txt', 'r') as arquivo:
        conteudo = arquivo.readlines()
    num_registro = 0

    while num_registro < len(conteudo):
        if cpf in conteudo[num_registro].split():
            registro = conteudo[num_registro].split('\t')
            print('CPF', registro[0])
            print('Nome', registro[1])
            print('Idade', registro[2])
            print('Sexo', registro[3])
            print('Nacionalidade', registro[4])
            if input('Deseja alterar o registro? (S/N').upper() == 'S':
                registro[0] = input('CPF: ')
                registro[1] = input('Nome: ')
                registro[2] = input('Idade: ')
                registro[3] = input('Sexo: ')
                registro[4] = input('Nacionalidade: ')
                conteudo[num_registro] = '\t'.join(registro)

                with open ('registro.txt', 'w') as arquivo:
                    arquivo.write("".join(conteudo))
                print('Registro atualizado com sucesso')
                break
            else:
                print('Cancelado pelo usuário')
                break
        else:
            print('Registro não encontrado') 
            break
main()

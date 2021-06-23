# import csv


# with open('texto.csv', 'r') as arquivo:
#     conteudo = csv.reader(arquivo, delimiter=',')
#     cabecalho = next(conteudo)
#     informao01 = next(conteudo)
#     restante_info = []
#     for linha in conteudo:
#         restante_info.append(linha)
# print(cabecalho)
# print(informao01)
# print(restante_info)

import json
import requests

# cep = input('Informe o CEP')

# viacep = 'https://viacep.com.br/ws/{cep}/json'
# requisicao = requests.get(viacep)
# conteudo = requisicao.content

# with open('arquivo.json', 'wb') as jsonfile:
#     jsonfile.write(conteudo)


# from defusedxml import ElementTree as ET

# #Carregando o arquivo
# arquivo_xml = ET.parse('arquivo.xml')

# #Acessando a primeira tag
# root = arquivo_xml.getroot()

# #Interando por todas as tags da root
# for elemento in root:
#     print(elemento.tag, elemento.text)

# print('========================')

# for time in root.find('times'):
#     print(time.tag, time.attrib)

# print('========================')

# for time in root.find('times'):
#     print(time.tag, time.attrib):
#     for jogador in time:

#     if time.attrib.get('nome') == 'Palmeiras':
#         print(time.find('*').tag, time.find('*').text)
        
from xml.etree.ElementTree import Element, SubElement, Comment, ElementTree

# Estrutura raiz do xml

raiz = Element('cadastro')

# Add comentarios ao xml
raiz.append(Comment('Cadastro de usuarios da locadora xpto'))

# Add elementos à arvore:

#Subelement nome
nome = SubElement(raiz, 'nome')
nome.text = 'Carlos Silva'

#Subelememt cpf
cpf = SubElement(raiz, 'cpf')
cpf.text = '089.125.111-95'

#Subelement endereço
endereco = SubElement(raiz, 'endereco')
endereco.text = 'Rua Maria da Graça, 156 - Jd Peri - SP'

#Subelement contato
contato = SubElement(raiz, 'contato')

#Elemento com Subelemento
telefone = SubElement(contato, 'telefone')
telefone.text = '(11) 953582497'

email = SubElement(contato, 'email')
email.text = 'carlos.silva@email.com'

# Gerar o arquivo xml
ElementTree(raiz).write('cadastro.xml')
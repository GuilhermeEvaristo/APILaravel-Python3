#Script para consumir API
#Linguagem utilizada : Python3
#Created by Jhonatas Rodrigues
#

import requests
import json
import os

# Request Area
data = requests.get('http://localhost:8000/api/produtos')
binary = data.content
output = json.loads(binary)
# Menu Area
os.system('clear')
def menu():
        print("--> Bem vindo ao apipy 0.9 <--")
        print( "(Menu)")
        print( ">> Use (1) Para Ver Produtos")
        print( ">> Use (2) Para Inserir Produto")
        print( ">> Use (3) Para Atualizar Produtos")
        print( ">> Use (4) Para Deletar Produtos")
        print( ">> Use (0) Para Abortar :/")
menu()
valor = input('Resposta :')
if valor == '1':
    os.system('clear')
    x = 0
    print("\n-----Produtos encontrados-----\n")
    for item in output['data']:
        print('>> Id:',item['id'],'\n>> Nome: ', item['name'], '\n>> Descrição :', item['description'], '\n>> Categoria :', item['categorias']['name'])
elif valor == '2' :
    os.system('clear')
    print(" >> Use (1) Categoria Comida")
    print(" >> Use (2) Categoria Bebida")
    categoria = input('Digite o Número da Categoria: ')
    nome = input("Digite o Nome do Produto :")
    desc = input("Digite a Descrição do Produto :")
    requests.post('http://localhost:8000/api/produtos', data = {'name':nome, 'description': desc, 'categoria_id':categoria})
elif valor == '4':
    os.system('clear')
    print(" >> Use (1) Deletar Apenas Um Produto")
    print(" >> Use (2) Para Deletar Todos os Produtos")
    print(" >> Use (0) Para Retornar ao Menu")
    resposta = input("Resposta :")
    if resposta == '1':
        produtoId = input('Digite o Id do Produto :')
        requests.delete('http://localhost:8000/api/produtos/' + produtoId)
    elif resposta == '2':
        requests.delete('http://localhost:8000/api/produtos')
    else :
        Menu()
elif valor == '3':
    os.system('clear')
    print(" >> Use (1) Categoria Comida")
    print(" >> Use (2) Categoria Bebida")
    identifier = input('Digite o ID do Produto Que Você Deseja Alterar : ')
    categoriaN = input('Nova Categoria: ')
    title = input('Novo Titulo : ')
    des = input('Nova Descrição : ')
    requests.put('http://localhost:8000/api/produtos/' + identifier , data = {'id': identifier, 'name':title, 'description': des, 'categoria_id':categoriaN})
else :
    print("By by :)")
#Percorrendo dados

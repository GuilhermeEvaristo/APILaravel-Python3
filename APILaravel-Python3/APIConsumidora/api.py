#Script para consumir API
#Linguagem utilizada : Python3
#Created by Jhonatas Rodrigues
#

import requests
import json
import os

# Request Area
data = requests.get('http://localhost:8000/api/bandas')
binary = data.content
output = json.loads(binary)
# Menu Area
os.system('clear')
def menu():
        print("--> Bem vindo <--")
        print( "(Menu)")
        print( ">> Use (1) Para Ver Bandas")
        print( ">> Use (2) Para Inserir Banda")
        print( ">> Use (3) Para Atualizar Bandas")
        print( ">> Use (4) Para Deletar Bandas")
        print( ">> Use (0) Para Abortar :/")
menu()
valor = input('Resposta :')
if valor == '1':
    os.system('clear')
    x = 0
    print("\n-----Bandas encontrados-----\n")
    for item in output['data']:
        print('>> Id:',item['id'],'\n>> Nome: ', item['name'], '\n>> Descrição :', item['description'], '\n>> Categoria :', item['categorias']['name'])
elif valor == '2' :
    os.system('clear')
    print(" >> Use (1) Categoria Gospel")
    print(" >> Use (2) Categoria Sertanejo")
    categoria = input('Digite o Número da Categoria: ')
    nome = input("Digite o Nome da Banda :")
    desc = input("Digite a Descrição da Banda :")
    requests.post('http://localhost:8000/api/bandas', data = {'name':nome, 'description': desc, 'categoria_id':categoria})
elif valor == '4':
    os.system('clear')
    print(" >> Use (1) Deletar Apenas Uma Banda")
    print(" >> Use (2) Para Deletar Todas as Bandas")
    print(" >> Use (0) Para Retornar ao Menu")
    resposta = input("Resposta :")
    if resposta == '1':
        produtoId = input('Digite o Id da Banda :')
        requests.delete('http://localhost:8000/api/bandas/' + bandaId)
    elif resposta == '2':
        requests.delete('http://localhost:8000/api/bandas')
    else :
        Menu()
elif valor == '3':
    os.system('clear')
    print(" >> Use (1) Categoria Gospel")
    print(" >> Use (2) Categoria Sertanejo")
    identifier = input('Digite o ID da Banda Que Você Deseja Alterar : ')
    categoriaN = input('Nova Categoria: ')
    title = input('Novo Titulo : ')
    des = input('Nova Descrição : ')
    requests.put('http://localhost:8000/api/bandas/' + identifier , data = {'id': identifier, 'name':title, 'description': des, 'categoria_id':categoriaN})
else :
    print("Flw :)")
#Percorrendo dados

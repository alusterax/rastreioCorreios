from sys import exit
import Funcoes

def menu():
    opcoes = ["Rastrear encomenda","Adicionar nova encomenda","Deletar Encomenda","Listar Encomendas","Sair"]
    print ('\n - - - - - - Correios - - - - - -')
    for idx,op in enumerate(opcoes):
        print (f'{idx+1} - {op}')
    ans = input ('\nEscolha uma opção: ')
    if (ans == '1'): 
        Funcoes.rastrear()
        menu()
    if (ans == '2'): 
        Funcoes.adicionar()
        menu()
    if (ans == '3'):
        Funcoes.deletar()
        menu()
    if (ans == '4'):
        Funcoes.listar()
        menu()
    else: 
        exit(0)

def start():
    menu()

start()
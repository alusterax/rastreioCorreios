from urllib3 import PoolManager,disable_warnings
from json import loads,dumps

def rastrear(codigo):
    disable_warnings()
    http = PoolManager()
    r = http.request('GET', 'https://linketrack.com/'+codigo+'/json')
    return r.data

def mostrar(a):
    print ('\nStatus:\n')
    campos = ['data', 'hora', 'local', 'status']
    for evento in a['eventos']:
        print('\n'.join([evento[campo] for campo in campos])+'\n--------------')

def start():
    inp = input('\nDigite o código de rastreamento:\n')
    dados = loads(rastrear(inp))
    mostrar(dados)

def startExistente(objeto):
    inp = objeto["codigo"]
    print (f'\n{objeto["nome"]}')
    dados = loads(rastrear(inp))
    mostrar(dados)
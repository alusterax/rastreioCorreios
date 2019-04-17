import urllib3
import json

def rastrear(codigo):
    http = urllib3.PoolManager()
    r = http.request('GET', 'https://linketrack.com/'+codigo+'/json')
    return r.data

def mostrar(a):
    campos = ['data', 'hora', 'local', 'status']
    for evento in a['eventos']:
        print('\n'.join([evento[campo] for campo in campos])+'\n------')

inp = input('\nDigite o código de rastreamento:\n')

dados = json.loads(rastrear(inp))

mostrar(dados)

import urllib3
import json

def rastrear(codigo):
    http = urllib3.PoolManager()
    r = http.request('GET', 'https://linketrack.com/'+codigo+'/json')
    return r.data

def mostrar(a):
    print('Mais recente primeiro:')
    for evento in a['eventos']:
        print('----------------\n'+evento['data']+'\n'+evento['hora']+'\n'+evento['local']+'\n'+evento['status'])

inp = input('\nDigite o código de rastreamento:\n')

dados = json.loads(rastrear(inp))

mostrar(dados)

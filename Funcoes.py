from pprint import pprint
import Rastreio
import Objetos

def rastrear():
    Objetos.verifyIfExists()
    objeto = Objetos.abrir()
    opcoes = ["Existente","Manual","Voltar"]

    for idx,op in enumerate(opcoes):
        print (f'{idx+1} - {op}')

    ans = input ('\nEscolha um tipo de encomenda: ')

    if (ans == '1'):
        if (len(objeto["encomendas"]) == 0):
            print('Não há encomendas cadastradas!\n')
            rastrear()
        else:
            for idx,enc in enumerate(objeto["encomendas"]):
                print(f'\n{idx} - Codigo: {enc["codigo"]}')
                print(f'    Nome: {enc["nome"]}')
            ans = input ('\nEscolha uma encomenda: ')
            Rastreio.startExistente(objeto["encomendas"][int(ans)])

    if (ans == '2'):
        Rastreio.start()

def adicionar():
    objNew = {}
    objNew["codigo"] = input ('Digite o código\n')
    objNew["nome"] = input ('Digite um nome:\n')
    obj = Objetos.abrir()
    obj["encomendas"].append(objNew)
    Objetos.salvar(obj)
    print ("\nObjeto adicionado!")

def deletar():
    objeto = Objetos.abrir()
    for idx,enc in enumerate(objeto["encomendas"]):
        print(f'\n{idx} - Codigo: {enc["codigo"]}')
        print(f'    Nome: {enc["nome"]}')
    ans = input ('\nEscolha uma encomenda: ')
    del objeto["encomendas"][int(ans)]
    Objetos.salvar(objeto)

def listar():
    objeto = Objetos.abrir()
    print('\n - - - - - Lista de encomendas - - - - - -\n')
    for idx,enc in enumerate(objeto["encomendas"]):
        print(f'\n{idx} - Codigo: {enc["codigo"]}')
        print(f'    Nome: {enc["nome"]}')
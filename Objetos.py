import json
import os.path

def salvar(objeto):
    with open("objeto.json",'w') as saida:
        json.dump (objeto,saida) 

def abrir():
    with open("objeto.json") as objetoJson:
        dadosObjeto = json.load (objetoJson)
    return dadosObjeto

def createNewFile():
    newFile = {
        "encomendas" : []
    }
    salvar(newFile)

def verifyIfExists():
    exists = os.path.exists('objeto.json')
    if (not exists):
        createNewFile()
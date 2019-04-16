#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import urllib3
import json


# In[ ]:


def rastrear(codigo):
    http = urllib3.PoolManager()
    r = http.request('GET', 'https://linketrack.com/'+codigo+'/json')
    return r.data


# In[ ]:


def mostrar(a):
    print('Mais recente primeiro:')
    for evento in a['eventos']:
        print('----------------\n'+evento['data']+'\n'+evento['hora']+'\n'+evento['local']+'\n'+evento['status'])


# In[ ]:


inp = input('\nDigite o código de rastreamento:\n')


# In[ ]:


dados = json.loads(rastrear(inp))


# In[ ]:


mostrar(dados)


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
    campos = ['data', 'hora', 'local', 'status']
    for evento in a['eventos']:
        print('\n'.join([evento[campo] for campo in campos])+'\n------')


# In[ ]:


inp = input('\nDigite o código de rastreamento:\n')


# In[ ]:


dados = json.loads(rastrear(inp))


# In[ ]:


mostrar(dados)


import uFirebase

fb = uFirebase.uFirebase('https://micro-py.firebaseio.com/')

# Caminho no banco de dados 
path = 'esp/'

# Dado a ser inserido 
data = {
    'greeting': 'Hello from ESP!'
}
    
fb.put(path, data)



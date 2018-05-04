import uFirebase

db = uFirebase.uFirebase('https://micro-py.firebaseio.com')

# Caminho no banco de dados 
path = '/coisa'

# Dado a ser inserido 
data = {
    'greeting': 'Hello from ESP!'
}

db.put(path, data)



# importando o SQLite
import sqlite3 as lite

# Criando conexão
con = lite.connect('AcervoBiblioteca.db')


# Criando tabela
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE AcervoBiblioteca (id INTEGER PRIMARY KEY AUTOINCREMENT,material TEXT, codigo_titulo INTEGER, titulo TEXT, numero_de_chamada INTEGER, data_publicacao TEXT,  autor TEXT, forma_aquisicao TEXT, data_aquisicao TEXT, fornecedor TEXT, preco DECIMAL)")

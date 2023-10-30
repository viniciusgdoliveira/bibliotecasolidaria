import sys
import sqlite3 as lite
from datetime import datetime


# Criando conexão
con = lite.connect('AcervoBiblioteca.db')

# Inserir AcervoBiblioteca
def inserir_form(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO AcervoBiblioteca (material, codigo_titulo, titulo, numero_de_chamada, data_publicacao, autor, forma_aquisicao, data_aquisicao, fornecedor, preco) VALUES (?,?,?,?,?,?,?,?,?,?)"
        cur.execute(query, i)


# Deletar AcervoBiblioteca
def deletar_form(i):
    
    with con:
        cur = con.cursor()
        query = "DELETE FROM AcervoBiblioteca WHERE id=?"
        cur.execute(query, i)


# Atualizar AcervoBiblioteca
def atualizar_form(i):
    with con:
        cur = con.cursor()
        query = "UPDATE AcervoBiblioteca SET material=?, codigo_titulo=?, titulo=?, numero_de_chamada=?, data_publicacao=?, autor=?, forma_aquisicao=?, data_aquisicao=?, fornecedor=?, preco=? WHERE id=?"
        cur.execute(query, i)


# Ver AcervoBiblioteca
def ver_form():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM AcervoBiblioteca")
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)
    return lista_itens


# Ver Itens
def ver_iten(id):
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM AcervoBiblioteca WHERE id=?",(id))
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)
    return lista_itens

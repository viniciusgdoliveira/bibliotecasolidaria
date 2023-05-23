from itertools import count
from tkinter import *
from tkinter import scrolledtext
from tkinter import Tk, StringVar, ttk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import filedialog as fd



################# tkdata_publicacaoendar ###############
from tkcalendar import Calendar, DateEntry
from datetime import date

from PIL import Image, ImageTk



################ importando view ######

from view import *



################# cores ###############

co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # autor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#3fbfb9"   # verde
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde
c10 = "#89181C"   # + vermelho cesusc

################# criando janela ###############

janela = Tk ()
janela.title ("")
janela.geometry('900x600')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")
style.configure("Treeview", highlightthickness=0, bd=0, font=('calibri', 9)) # Modify the font of the body



################# Frames ####################

frameCima = Frame(janela, width=1043, height=50, bg=co1,  relief="flat",)
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela,width=1043, height=303,bg=co1, pady=20, relief="flat")
frameMeio.grid(row=1, column=0,pady=1, padx=0, sticky=NSEW)

frameDireita = Frame(janela,width=1043, height=300,bg=co1, relief="flat")
frameDireita.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)

# abrindo imagem
app_img  = Image.open(r'images\Cesusc.png')
app_img = app_img.resize((45, 45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text=" Biblioteca Solidária", width=900, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'),bg=co1, fg=c10 )
app_logo.place(x=0, y=0)

global tree

# funcao inserir
def inserir():
    global imagem,imagem_string, l_imagem
    material = e_material.get()
    codigo_titulo = e_codigo_titulo.get()
    titulo = e_titulo.get()
    numero_de_chamada = e_numero_de_chamada.get()
    data_publicacao = e_data_publicacao.get()
    autor = e_autor.get()
    forma_aquisicao = e_forma_aquisicao.get()
    data_aquisicao = e_data_aquisicao.get()
    fornecedor = e_fornecedor.get()
    preco = e_preco.get()

    
    lista_inserir = [material, codigo_titulo, titulo, numero_de_chamada, data_publicacao, autor, forma_aquisicao, data_aquisicao, fornecedor, preco]
    
    for i in lista_inserir:
        if i=='':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return
        
    inserir_form(lista_inserir)

    messagebox.showinfo(
        'Sucesso', 'Os dados foram inseridos com sucesso')
        
    e_material.delete(0, 'end')
    e_codigo_titulo.delete(0, 'end')
    e_titulo.delete(0, 'end')
    e_numero_de_chamada.delete(0, 'end')
    e_data_publicacao.delete(0, 'end')
    e_autor.delete(0, 'end')
    e_forma_aquisicao.delete(0, 'end')
    e_data_aquisicao.delete(0, 'end')
    e_fornecedor.delete(0, 'end')
    e_preco.delete(0, 'end')   
    
    for widget in frameDireita.winfo_children():
        widget.destroy()

    mostrar()


# funcao atualizar
def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        autor = treev_lista[0]
        
        e_material.delete(0, 'end')
        e_codigo_titulo.delete(0, 'end')
        e_titulo.delete(0, 'end')
        e_numero_de_chamada.delete(0, 'end')
        e_data_publicacao.delete(0, 'end')
        e_autor.delete(0, 'end')
        e_forma_aquisicao.delete(0, 'end')
        e_data_aquisicao.delete(0, 'end')
        e_fornecedor.delete(0, 'end')
        e_preco.delete(0, 'end')    
        
        id = int(treev_lista[0])
        e_material.insert(0, treev_lista[1])
        e_codigo_titulo.insert(0, treev_lista[2])
        e_titulo.insert(0, treev_lista[3])
        e_numero_de_chamada.insert(0, treev_lista[4])
        e_data_publicacao.insert(0, treev_lista[5])
        e_autor.insert(0, treev_lista[6])
        e_forma_aquisicao.insert(0, treev_lista[7])
        e_data_aquisicao.insert(0, treev_lista[8])
        e_fornecedor.insert(0, treev_lista[9])
        e_preco.insert(0, treev_lista[10])

        def update():
            global imagem,imagem_string, l_imagem
            material = e_material.get()
            codigo_titulo = e_codigo_titulo.get()
            titulo = e_titulo.get()
            numero_de_chamada = e_numero_de_chamada.get()
            data_publicacao = e_data_publicacao.get()
            autor = e_autor.get()
            forma_aquisicao = e_forma_aquisicao.get()
            data_aquisicao = e_data_aquisicao.get()
            fornecedor = e_fornecedor.get()
            preco = e_preco.get()
        
            lista_atualizar = [material, codigo_titulo, titulo, numero_de_chamada, data_publicacao, autor, forma_aquisicao, data_aquisicao, fornecedor, preco]
            
            for i in lista_atualizar:
                if i=='':
                    messagebox.showerror('Erro', 'Preencha todos os campos')
                    return
            
            atualizar_form(lista_atualizar)

            messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso')
            
            e_material.delete(0, 'end')
            e_codigo_titulo.delete(0, 'end')
            e_titulo.delete(0, 'end')
            e_numero_de_chamada.delete(0, 'end')
            e_data_publicacao.delete(0, 'end')
            e_autor.delete(0, 'end')
            e_forma_aquisicao.delete(0, 'end')
            e_data_aquisicao.delete(0, 'end')
            e_fornecedor.delete(0, 'end')
            e_preco.delete(0, 'end')
            
            botao_confirmar.destroy()
            
            for widget in frameDireita.winfo_children():
                widget.destroy()

            mostrar()
        botao_confirmar = Button(frameMeio, command=update, text="Confirmar".upper(), width=13, height=1, bg=co2, fg=co1,font=('ivy 8 bold'),relief=RAISED, overrelief=RIDGE)
        botao_confirmar.place(x=330, y=185)
 

    except IndexError:
        messagebox.showerror(
            'Erro', 'Seleciona um dos dados na tabela')
        
    
# funcao deletar
def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        autor = treev_lista[0]
        
        deletar_form([autor])
                
        messagebox.showinfo(
            'Sucesso', 'Os dados foram deletados com sucesso')


        for widget in frameDireita.winfo_children():
            widget.destroy()

        mostrar()

    except IndexError:
        messagebox.showerror(
            'Erro', 'Seleciona um dos dados na tabela')
def ver_imagem():
    global l_imagem, imagem, imagem_string
    
    treev_dados = tree.focus()
    treev_dicionario = tree.item(treev_dados)
    treev_lista = treev_dicionario['values']
    autor = [int(treev_lista[0])]
    
    iten = ver_iten(autor)
        
    

l_material = Label(frameMeio, text="Material", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_material.place(x=10, y=10)
e_material = Entry(frameMeio, width=30, justify='left',relief="solid")
e_material.place(x=130, y=11)

l_codigo_titulo = Label(frameMeio, text="Código Título", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_codigo_titulo.place(x=10, y=40)
e_codigo_titulo = Entry(frameMeio, width=30, justify='left',relief="solid")
e_codigo_titulo.place(x=130, y=41)

l_titulo = Label(frameMeio, text="Título", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_titulo.place(x=10, y=70)
e_titulo = Entry(frameMeio, width=30, justify='left',relief="solid")
e_titulo.place(x=130, y=71)

l_numero_de_chamada = Label(frameMeio, text="Número de Chamada", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_numero_de_chamada.place(x=10, y=100)
e_numero_de_chamada = Entry(frameMeio, width=30, justify='left',relief="solid")
e_numero_de_chamada.place(x=130, y=101)

l_data_publicacao = Label(frameMeio, text="Data Publicação", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_data_publicacao.place(x=10, y=130)
e_data_publicacao = Entry(frameMeio, width=30, justify='left',relief="solid")
e_data_publicacao.place(x=130, y=131)

l_autor = Label(frameMeio, text="Autor", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_autor.place(x=450, y=10)
e_autor = Entry(frameMeio, width=30, justify='left',relief="solid")
e_autor.place(x=600, y=11)

l_forma_aquisicao = Label(frameMeio, text="Forma de Aquisição", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_forma_aquisicao.place(x=450, y=40)
e_forma_aquisicao = Entry(frameMeio, width=30, justify='left',relief="solid")
e_forma_aquisicao.place(x=600, y=41)

l_data_aquisicao = Label(frameMeio, text="Data de Aquisição", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_data_aquisicao.place(x=450, y=70)
e_data_aquisicao = Entry(frameMeio, width=30, justify='left',relief="solid")
e_data_aquisicao.place(x=600, y=71)

l_fornecedor = Label(frameMeio, text="Fornecedor", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_fornecedor.place(x=450, y=100)
e_fornecedor = Entry(frameMeio, width=30, justify='left',relief="solid")
e_fornecedor.place(x=600, y=101)

l_preco = Label(frameMeio, text="Preço", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_preco.place(x=450, y=130)
e_preco = Entry(frameMeio, width=30, justify='left',relief="solid")
e_preco.place(x=600, y=131)

# Botao Inserir
img_add  = Image.open(r'images\add.png')
img_add = img_add.resize((20, 20))
img_add = ImageTk.PhotoImage(img_add)
botao_inserir = Button(frameMeio, command=inserir,image=img_add, compound=LEFT, anchor=NW, text="   Adicionar".upper(), width=95, overrelief=RIDGE,  font=('ivy 8'),bg=co1, fg=co0 )
botao_inserir.place(x=330, y=10)


# Botao Atualizar
img_update  = Image.open(r'images\update.png')
img_update = img_update.resize((20, 20))
img_update = ImageTk.PhotoImage(img_update)
botao_atualizar = Button(frameMeio, command=atualizar,image=img_update, compound=LEFT, anchor=NW, text="   Atualizar".upper(), width=95, overrelief=RIDGE,  font=('ivy 8'),bg=co1, fg=co0 )
botao_atualizar.place(x=330, y=50)


# Botao Deletar
img_delete  = Image.open(r'images\delete.png')
img_delete = img_delete.resize((20, 20))
img_delete = ImageTk.PhotoImage(img_delete)
botao_deletar = Button(frameMeio, command=deletar,image=img_delete, compound=LEFT, anchor=NW, text="   Deletar".upper(), width=95, overrelief=RIDGE,  font=('ivy 8'),bg=co1, fg=co0 )
botao_deletar.place(x=330, y=90)

# Botao pesquisar Item
img_item  = Image.open(r'images\pesquisa.png')
img_item = img_item.resize((20, 20))
img_item = ImageTk.PhotoImage(img_item)
botao_ver = Button(frameMeio, command=ver_imagem,image=img_item, compound=LEFT, anchor=NW, text="   Pesquisar item".upper(), width=95, overrelief=RIDGE,  font=('ivy 8'),bg=co1, fg=co0 )
botao_ver.place(x=330, y=130)


################# frame tree ####################

# funcao para mostrar
def mostrar():

    # creating a treeview with dual scrollbars
    tabela_head = ['#Tombo','Material',  'Código Título','Título', 'Número da Chamada', 'Data Publicação','Autor', 'Forma de Aquisição','Data de Aquisição','Fornecedor','Preço']

    lista_itens = ver_form()
    
    global tree

    tree = ttk.Treeview(frameDireita, selectmode="extended",
                        columns=tabela_head, show="headings")
    # vertical scrollbar
    vsb = ttk.Scrollbar(
        frameDireita, orient="vertical", command=tree.yview)
    # horizontal scrollbar
    hsb = ttk.Scrollbar(
        frameDireita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameDireita.grid_rowconfigure(0, weight=12)

    hd=["center","center","center","center","center","center","center", 'center',"center","center","center"]
    h=[50,70,70,70,120,100,50, 120, 120, 70, 70]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in lista_itens:
        tree.insert('', 'end', values=item)
        
    quantidade = []
    for iten in lista_itens:
        quantidade.append(iten[6])
    

mostrar()
    

janela.mainloop ()
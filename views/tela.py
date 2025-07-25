from ast import Lambda
from cProfile import label
from datetime import date
from tkinter import messagebox
from tkinter import ttk
from tkinter .ttk import *
from tkinter import *
from PIL import Image, ImageTk

from models.crud import *

co0 ="#2e2d2b" #preto
co1 = "#feffff" # branco
co2 = "#4fa882" # verde
co3 = "#38576b" #valor
co4 = "#403d3d" #letra
co5 = "#e06636" # - profit
co6 = "#038cfc" #azul
co7 = "#3fbfb9" #verde
co8 = "#263238" #+verde
co9 = "#e9edf5" #+verde
co10 = "#6e8faf"
co11 = "#f2f4f2"
def iniciar_interface():
    # criando janela 
    janela = Tk()
    janela.title("")
    janela.geometry("770x330")
    janela.configure(background= co1)
    janela.resizable(width=FALSE, height=FALSE)

    style = Style(janela)
    style.theme_use("clam")

#Frames
    frameCima = Frame(janela, width=770, height=50,bg=co5, relief="flat")
    frameCima.grid(row=0, column=0, columnspan=2, sticky=NSEW)

    frameEsquerda = Frame(janela, width=150, height=265,bg=co4, relief="solid")
    frameEsquerda.grid(row=1, column=0, sticky=NSEW)

    frameDireita = Frame(janela, width=600, height=265,bg=co1, relief="raised")
    frameDireita.grid(row=1, column=1, sticky=NSEW)

    #logo 
    app_img = Image.open('icons/1.png')
    app_img = app_img.resize((40,40))
    app_img = ImageTk.PhotoImage(app_img)

    app_logo = Label(frameCima, image=app_img, width=1000, compound=LEFT, padx=5, anchor=NW, bg=co5, fg=co1)
    app_logo.place(x=5,y=0)

    app_ = Label(frameCima, text="Sistema de Gerenciamento de livros", width=1000, compound=LEFT, padx=5, anchor=NW,font=('Verdana 15 bold'), bg=co5, fg=co1)
    app_.place(x=50,y=7)

#Form novo usuario
    def novo_usuario():
        global img_salvar

        def add():
            first_name = e_p_nome.get()
            last_name = e_sobrenome.get()
            address = e_p_endereco.get()
            email = e_email.get()
            phone = e_numero.get()

            lista =[first_name, last_name, address, email, phone]

            for i in lista:
                if i =='':
                    messagebox.showerror('Erro', 'Preencha todos os campos')
                    return
                
            # adcionando os dados no banco
            insert_user(first_name, last_name, address, email, phone)

            messagebox.showinfo('Sucesso','Usuario adicionado com sucesso')
            # limpando os campos
            e_p_nome.delete(0,END)
            e_sobrenome.delete(0,END)
            e_p_endereco.delete(0,END)
            e_email.delete(0,END)
            e_numero.delete(0,END)


        app_ = Label(frameDireita, text="Inserir novo usuario", width=50, compound=LEFT, padx=5, pady=10,font=('Verdana 12'), bg=co1, fg= co4)
        app_.grid(row=0,column=0, columnspan=4, sticky=NSEW)
        app_linha = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1'),bg=co3, fg=co1)
        app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

        l_p_nome = Label(frameDireita, text="Primeiro nome", anchor=NW, font=('Ivy 10'), bg=co1, fg= co4)
        l_p_nome.grid(row=2,column=0, padx=5, pady=5, sticky=NSEW)
        e_p_nome = Entry(frameDireita, width=25, justify='left', relief='solid')
        e_p_nome.grid(row=2,column=1, padx=5, pady=5, sticky=NSEW)

        l_sobrenome = Label(frameDireita, text="Sobrenome", anchor=NW, font=('Ivy 10'), bg=co1, fg= co4)
        l_sobrenome.grid(row=3,column=0, padx=5, pady=5, sticky=NSEW)
        e_sobrenome = Entry(frameDireita, width=25, justify='left', relief='solid')
        e_sobrenome.grid(row=3,column=1, padx=5, pady=5, sticky=NSEW)

        l_p_endereco = Label(frameDireita, text="Endereco do usuario", anchor=NW, font=('Ivy 10'), bg=co1, fg= co4)
        l_p_endereco.grid(row=4,column=0, padx=5, pady=5, sticky=NSEW)
        e_p_endereco = Entry(frameDireita, width=25, justify='left', relief='solid')
        e_p_endereco.grid(row=4,column=1, padx=5, pady=5, sticky=NSEW)

        l_email = Label(frameDireita, text="Email", anchor=NW, font=('Ivy 10'), bg=co1, fg= co4)
        l_email.grid(row=5,column=0, padx=5, pady=5, sticky=NSEW)
        e_email = Entry(frameDireita, width=25, justify='left', relief='solid')
        e_email.grid(row=5,column=1, padx=5, pady=5, sticky=NSEW)

        l_numero = Label(frameDireita, text="Numero de telefone", anchor=NW, font=('Ivy 10'), bg=co1, fg= co4)
        l_numero.grid(row=6,column=0, padx=5, pady=5, sticky=NSEW)
        e_numero = Entry(frameDireita, width=25, justify='left', relief='solid')
        e_numero.grid(row=6,column=1, padx=5, pady=5, sticky=NSEW)

        #Botao salvar
        img_salvar = Image.open('icons/disk.png')
        img_salvar = img_salvar.resize((18,18))
        img_salvar = ImageTk.PhotoImage(img_salvar)

        b_salvar = Button(frameDireita, command=add, image=img_salvar, compound=LEFT, width=100, anchor=NW, text=" Salvar", bg= co1, fg=co4, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
        b_salvar.grid(row=7,column=1, pady=5, sticky=NSEW)


# funcao ver usuarios
    def ver_usuarios():

        app_ = Label(frameDireita,text="Todos os usuários do banco de dados",width=50,compound=LEFT, padx=5,pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'),bg=co1, fg=co4)
        app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
        l_linha = Label(frameDireita, width=400, height=1,anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
        l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

        dados = get_users()

        # creating a treeview with dual scrollbars
        list_header = ['ID','Nome','Sobrenome','Endereco','Email','Telefone']
        
        global tree

        tree = ttk.Treeview(frameDireita, selectmode="extended",
                            columns=list_header, show="headings")
        # vertical scrollbar
        vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)

        # horizontal scrollbar
        hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)

        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        tree.grid(column=0, row=2, sticky='nsew')
        vsb.grid(column=1, row=2, sticky='ns')
        hsb.grid(column=0, row=3, sticky='ew')
        frameDireita.grid_rowconfigure(0, weight=12)

        hd=["nw","nw","nw","nw","nw","nw"]
        h=[20,80,80,120,120,76,100]
        n=0

        for col in list_header:
            tree.heading(col, text=col, anchor='nw')
            # adjust the column's width to the header string
            tree.column(col, width=h[n],anchor=hd[n])
            
            n+=1

        for item in dados:
            tree.insert('', 'end', values=item)



#Form novo livro
    def novo_livro():
        global img_salvar

        def add():
            titulo = e_p_titulo.get()
            autor = e_autor.get()
            editora = e_p_editora.get()
            ano = e_ano.get()
            isbn = e_isbn.get()

            lista =[titulo, autor, editora, ano, isbn]

            for i in lista:
                if i =='':
                    messagebox.showerror('Erro', 'Preencha todos os campos')
                    return
                
            # adcionando os dados no banco
            insert_book(titulo, autor, editora, ano, isbn)

            messagebox.showinfo('Sucesso','Livro adicionado com sucesso')
            # limpando os campos
            e_p_titulo.delete(0,END)
            e_autor.delete(0,END)
            e_p_editora.delete(0,END)
            e_ano.delete(0,END)
            e_isbn.delete(0,END)


        app_ = Label(frameDireita, text="Inserir novo livro", width=50, compound=LEFT, padx=5, pady=10,font=('Verdana 12'), bg=co1, fg= co4)
        app_.grid(row=0,column=0, columnspan=4, sticky=NSEW)
        app_linha = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1'),bg=co3, fg=co1)
        app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

        l_p_titulo = Label(frameDireita, text="Titulo do livro", anchor=NW, font=('Ivy 10'), bg=co1, fg= co4)
        l_p_titulo.grid(row=2,column=0, padx=5, pady=5, sticky=NSEW)
        e_p_titulo = Entry(frameDireita, width=25, justify='left', relief='solid')
        e_p_titulo.grid(row=2,column=1, padx=5, pady=5, sticky=NSEW)

        l_autor = Label(frameDireita, text="Autor do livro", anchor=NW, font=('Ivy 10'), bg=co1, fg= co4)
        l_autor.grid(row=3,column=0, padx=5, pady=5, sticky=NSEW)
        e_autor = Entry(frameDireita, width=25, justify='left', relief='solid')
        e_autor.grid(row=3,column=1, padx=5, pady=5, sticky=NSEW)

        l_p_editora = Label(frameDireita, text="Editora do livro", anchor=NW, font=('Ivy 10'), bg=co1, fg= co4)
        l_p_editora.grid(row=4,column=0, padx=5, pady=5, sticky=NSEW)
        e_p_editora = Entry(frameDireita, width=25, justify='left', relief='solid')
        e_p_editora.grid(row=4,column=1, padx=5, pady=5, sticky=NSEW)

        l_ano = Label(frameDireita, text="Ano de publicacao", anchor=NW, font=('Ivy 10'), bg=co1, fg= co4)
        l_ano.grid(row=5,column=0, padx=5, pady=5, sticky=NSEW)
        e_ano = Entry(frameDireita, width=25, justify='left', relief='solid')
        e_ano.grid(row=5,column=1, padx=5, pady=5, sticky=NSEW)

        l_isbn = Label(frameDireita, text="ISBN do livro", anchor=NW, font=('Ivy 10'), bg=co1, fg= co4)
        l_isbn.grid(row=6,column=0, padx=5, pady=5, sticky=NSEW)
        e_isbn = Entry(frameDireita, width=25, justify='left', relief='solid')
        e_isbn.grid(row=6,column=1, padx=5, pady=5, sticky=NSEW)

        #Botao salvar
        img_salvar = Image.open('icons/disk.png')
        img_salvar = img_salvar.resize((18,18))
        img_salvar = ImageTk.PhotoImage(img_salvar)

        b_salvar = Button(frameDireita, command=add, image=img_salvar, compound=LEFT, width=100, anchor=NW, text=" Salvar", bg= co1, fg=co4, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
        b_salvar.grid(row=7,column=1, pady=5, sticky=NSEW)


# funcao ver usuarios
    def ver_livros():

        app_ = Label(frameDireita,text="Todos os livros do banco de dados",width=50,compound=LEFT, padx=5,pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'),bg=co1, fg=co4)
        app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
        l_linha = Label(frameDireita, width=400, height=1,anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
        l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

        dados = listar_livros()

        # creating a treeview with dual scrollbars
        list_header = ['ID','Titulo','Autor','Editora','Ano','Isbn']
        
        global tree

        tree = ttk.Treeview(frameDireita, selectmode="extended",
                            columns=list_header, show="headings")
        # vertical scrollbar
        vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)

        # horizontal scrollbar
        hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)

        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        tree.grid(column=0, row=2, sticky='nsew')
        vsb.grid(column=1, row=2, sticky='ns')
        hsb.grid(column=0, row=3, sticky='ew')
        frameDireita.grid_rowconfigure(0, weight=12)

        hd=["nw","nw","nw","nw","nw","nw"]
        h=[20,80,80,120,120,76,100]
        n=0

        for col in list_header:
            tree.heading(col, text=col, anchor='nw')
            # adjust the column's width to the header string
            tree.column(col, width=h[n],anchor=hd[n])
            
            n+=1

        for item in dados:
            tree.insert('', 'end', values=item)


#Realizar emprestimo

    def realizar_emprestimo():
        global img_salvar

        def add():
            id_user = e_id_user.get()
            id_livro = e_id_livro.get()
            data_emprestimo = date.today().strftime("%Y-%m-%d")
            data_devolucao = None
     

            lista =[id_user, id_livro, data_emprestimo,data_devolucao]

            for i in lista:
                if i =='':
                    messagebox.showerror('Erro', 'Preencha todos os campos')
                    return
                
            # adcionando os dados no banco
            insert_loan(id_user, id_livro, data_emprestimo,data_devolucao)

            messagebox.showinfo('Sucesso','Emprestimo realizado com sucesso')
            # limpando os campos
            e_id_user.delete(0,END)
            e_id_livro.delete(0,END)



        app_ = Label(frameDireita, text="Realizar um emprestimo", width=50, compound=LEFT, padx=5, pady=10,font=('Verdana 12'), bg=co1, fg= co4)
        app_.grid(row=0,column=0, columnspan=4, sticky=NSEW)
        app_linha = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1'),bg=co3, fg=co1)
        app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

        l_id_user = Label(frameDireita, text="Digite o ID do usuario", anchor=NW, font=('Ivy 10'), bg=co1, fg= co4)
        l_id_user.grid(row=2,column=0, padx=5, pady=5, sticky=NSEW)
        e_id_user = Entry(frameDireita, width=25, justify='left', relief='solid')
        e_id_user.grid(row=2,column=1, padx=5, pady=5, sticky=NSEW)

        l_id_livro = Label(frameDireita, text="Digite o ID do Livro", anchor=NW, font=('Ivy 10'), bg=co1, fg= co4)
        l_id_livro.grid(row=3,column=0, padx=5, pady=5, sticky=NSEW)
        e_id_livro = Entry(frameDireita, width=25, justify='left', relief='solid')
        e_id_livro.grid(row=3,column=1, padx=5, pady=5, sticky=NSEW)

        

        #Botao salvar
        img_salvar = Image.open('icons/disk.png')
        img_salvar = img_salvar.resize((18,18))
        img_salvar = ImageTk.PhotoImage(img_salvar)

        b_salvar = Button(frameDireita, command=add, image=img_salvar, compound=LEFT, width=100, anchor=NW, text=" Salvar", bg= co1, fg=co4, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
        b_salvar.grid(row=7,column=1, pady=5, sticky=NSEW)


#ver livros emprestados
    def ver_livros_emprestados():

        app_ = Label(frameDireita,text="Todos os livros Emprestados",width=50,compound=LEFT, padx=5,pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'),bg=co1, fg=co4)
        app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
        l_linha = Label(frameDireita, width=400, height=1,anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
        l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

        dados = get_books_on_lean()

        # creating a treeview with dual scrollbars
        list_header = ['ID','Titulo','Nome do Usuario','D.Emprestimo','D.Devolucao']
        
        global tree

        tree = ttk.Treeview(frameDireita, selectmode="extended",
                            columns=list_header, show="headings")
        # vertical scrollbar
        vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)

        # horizontal scrollbar
        hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)

        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        tree.grid(column=0, row=2, sticky='nsew')
        vsb.grid(column=1, row=2, sticky='ns')
        hsb.grid(column=0, row=3, sticky='ew')
        frameDireita.grid_rowconfigure(0, weight=12)

        hd = ["nw", "nw", "nw", "nw", "nw"]
        h = [20, 120, 140, 120, 100]

        n=0

        for col in list_header:
            tree.heading(col, text=col, anchor='nw')
            # adjust the column's width to the header string
            tree.column(col, width=h[n],anchor=hd[n])
            
            n+=1

        for item in dados:
            tree.insert('', 'end', values=item)

#Devolucao do livro
    def realizar_devolucao():
            global img_salvar

            def add():
                id_emprestimo = e_id_emprestimo.get()
                data_devolucao = date.today().strftime("%Y-%m-%d")
        

                lista =[id_emprestimo,data_devolucao]

                for i in lista:
                    if i =='':
                        messagebox.showerror('Erro', 'Preencha todos os campos')
                        return
                    
                # adcionando os dados no banco
                update_loan_return_date(id_emprestimo,data_devolucao)

                messagebox.showinfo('Sucesso','Devolucao realizado com sucesso')
                # limpando os campos
                e_id_emprestimo.delete(0,END)
                



            app_ = Label(frameDireita, text="Realizar uma Devolucao", width=50, compound=LEFT, padx=5, pady=10,font=('Verdana 12'), bg=co1, fg= co4)
            app_.grid(row=0,column=0, columnspan=4, sticky=NSEW)
            app_linha = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1'),bg=co3, fg=co1)
            app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

            l_id_emprestimo = Label(frameDireita, text="Digite o ID do Emprestimo", anchor=NW, font=('Ivy 10'), bg=co1, fg= co4)
            l_id_emprestimo.grid(row=2,column=0, padx=5, pady=5, sticky=NSEW)
            e_id_emprestimo = Entry(frameDireita, width=25, justify='left', relief='solid')
            e_id_emprestimo.grid(row=2,column=1, padx=5, pady=5, sticky=NSEW)

            #Botao salvar
            img_salvar = Image.open('icons/disk.png')
            img_salvar = img_salvar.resize((18,18))
            img_salvar = ImageTk.PhotoImage(img_salvar)

            b_salvar = Button(frameDireita, command=add, image=img_salvar, compound=LEFT, width=100, anchor=NW, text=" Salvar", bg= co1, fg=co4, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
            b_salvar.grid(row=7,column=1, pady=5, sticky=NSEW)

#Funcao de controle do Menu
    def control(i):
        #novo usuario
        if i == 'novo_usuario':
            for widget in frameDireita.winfo_children():
                widget.destroy()

            # chamando a funcao novo usuario
            novo_usuario()   
        
        #ver usuario
        if i == 'ver_usuarios':
            for widget in frameDireita.winfo_children():
                widget.destroy()

            # chamando a funcao novo usuario
            ver_usuarios()
              
        #novo livro

        if i == 'novo_livro':
            for widget in frameDireita.winfo_children():
                widget.destroy()

            # chamando a funcao novo usuario
            novo_livro() 
                #ver usuario

        if i == 'ver_livros':
            for widget in frameDireita.winfo_children():
                widget.destroy()

        
            ver_livros()

        if i == 'realizar_emprestimo':
            for widget in frameDireita.winfo_children():
                widget.destroy()

        
            realizar_emprestimo()

        if i == 'ver_livros_emprestados':
            for widget in frameDireita.winfo_children():
                widget.destroy()

            ver_livros_emprestados()

        if i == 'realizar_devolucao':
            for widget in frameDireita.winfo_children():
                widget.destroy()

            realizar_devolucao()

        
            
            
        

#Menu
    #Novo Usuario
    img_usuario = Image.open('icons/user.png')
    img_usuario = img_usuario.resize((18,18))
    img_usuario = ImageTk.PhotoImage(img_usuario)

    b_usuario = Button(frameEsquerda,command=lambda:control('novo_usuario'), image=img_usuario, compound=LEFT, anchor=NW, text=" Novo usuario", bg= co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_usuario.grid(row=0, column=0, sticky=NSEW, padx=5, pady=6)

    #Novo livro
    img_novo_livro = Image.open('icons/add.png')
    img_novo_livro = img_novo_livro.resize((18,18))
    img_novo_livro = ImageTk.PhotoImage(img_novo_livro)

    b_novo_livro = Button(frameEsquerda,command=lambda:control('novo_livro'), image=img_novo_livro, compound=LEFT, anchor=NW, text=" Novo livro", bg= co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_novo_livro.grid(row=1, column=0, sticky=NSEW, padx=5, pady=6)

    #Ver livro
    img_ver_livro = Image.open('icons/1.png')
    img_ver_livro = img_ver_livro.resize((18,18))
    img_ver_livro = ImageTk.PhotoImage(img_ver_livro)

    b_ver_livro = Button(frameEsquerda,command=lambda:control('ver_livros'), image=img_ver_livro, compound=LEFT, anchor=NW, text=" Exibir todos os livros", bg= co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_ver_livro.grid(row=2, column=0, sticky=NSEW, padx=5, pady=6)

    #Ver Usuarios
    img_ver_usuario = Image.open('icons/user.png')
    img_ver_usuario = img_ver_usuario.resize((18,18))
    img_ver_usuario = ImageTk.PhotoImage(img_ver_usuario)

    b_ver_usuario = Button(frameEsquerda, command=lambda:control('ver_usuarios'), image=img_ver_usuario, compound=LEFT, anchor=NW, text=" Exibir todos usuario", bg= co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_ver_usuario.grid(row=3, column=0, sticky=NSEW, padx=5, pady=6)

    #Realizar emprestimo
    img_emprestimo = Image.open('icons/add.png')
    img_emprestimo = img_emprestimo.resize((18,18))
    img_emprestimo = ImageTk.PhotoImage(img_emprestimo)

    b_emprestimo = Button(frameEsquerda, command=lambda:control('realizar_emprestimo'), image=img_emprestimo, compound=LEFT, anchor=NW, text=" Realizar emprestimo", bg= co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_emprestimo.grid(row=4, column=0, sticky=NSEW, padx=5, pady=6)

    #Devolucao de um livro
    img_devolucao = Image.open('icons/update.png')
    img_devolucao = img_devolucao.resize((18,18))
    img_devolucao = ImageTk.PhotoImage(img_devolucao)

    b_devolucao = Button(frameEsquerda,command=lambda:control('realizar_devolucao'), image=img_devolucao, compound=LEFT, anchor=NW, text=" Realizar devolucao do livro", bg= co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_devolucao.grid(row=5, column=0, sticky=NSEW, padx=5, pady=6)

    #Exibir livros emprestados
    img_livros_emprestados = Image.open('icons/cart.png')
    img_livros_emprestados = img_livros_emprestados.resize((18,18))
    img_livros_emprestados = ImageTk.PhotoImage(img_livros_emprestados)

    b_livros_emprestados = Button(frameEsquerda,command=lambda:control('ver_livros_emprestados'), image=img_livros_emprestados, compound=LEFT, anchor=NW, text=" Livros emprestados", bg= co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_livros_emprestados.grid(row=6, column=0, sticky=NSEW, padx=5, pady=6)
    



    janela.mainloop()

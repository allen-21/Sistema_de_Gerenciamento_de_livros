from ast import Lambda
from cProfile import label
from tkinter .ttk import *
from tkinter import *
from PIL import Image, ImageTk

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

        b_salvar = Button(frameDireita, image=img_salvar, compound=LEFT, width=100, anchor=NW, text=" Salvar", bg= co1, fg=co4, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
        b_salvar.grid(row=7,column=1, pady=5, sticky=NSEW)


#Funcao de controle do Meno
    def control(i):
        #novo usuario
        if i == 'novo_usuario':
            for widget in frameDireita.winfo_children():
                widget.destroy()

            # chamando a funcao novo usuario
            novo_usuario()   

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

    b_novo_livro = Button(frameEsquerda, image=img_novo_livro, compound=LEFT, anchor=NW, text=" Novo livro", bg= co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_novo_livro.grid(row=1, column=0, sticky=NSEW, padx=5, pady=6)

    #Ver livro
    img_ver_livro = Image.open('icons/1.png')
    img_ver_livro = img_ver_livro.resize((18,18))
    img_ver_livro = ImageTk.PhotoImage(img_ver_livro)

    b_ver_livro = Button(frameEsquerda, image=img_ver_livro, compound=LEFT, anchor=NW, text=" Exibir todos os livros", bg= co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_ver_livro.grid(row=2, column=0, sticky=NSEW, padx=5, pady=6)

    #Ver Usuarios
    img_ver_usuario = Image.open('icons/user.png')
    img_ver_usuario = img_ver_usuario.resize((18,18))
    img_ver_usuario = ImageTk.PhotoImage(img_ver_usuario)

    b_ver_usuario = Button(frameEsquerda, image=img_ver_usuario, compound=LEFT, anchor=NW, text=" Exibir todos usuario", bg= co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_ver_usuario.grid(row=3, column=0, sticky=NSEW, padx=5, pady=6)

    #Realizar emprestimo
    img_emprestimo = Image.open('icons/add.png')
    img_emprestimo = img_emprestimo.resize((18,18))
    img_emprestimo = ImageTk.PhotoImage(img_emprestimo)

    b_emprestimo = Button(frameEsquerda, image=img_emprestimo, compound=LEFT, anchor=NW, text=" Realizar emprestimo", bg= co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_emprestimo.grid(row=4, column=0, sticky=NSEW, padx=5, pady=6)

    #Devolucao de um livro
    img_devolucao = Image.open('icons/update.png')
    img_devolucao = img_devolucao.resize((18,18))
    img_devolucao = ImageTk.PhotoImage(img_devolucao)

    b_devolucao = Button(frameEsquerda, image=img_devolucao, compound=LEFT, anchor=NW, text=" Realizar devolucao do livro", bg= co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_devolucao.grid(row=5, column=0, sticky=NSEW, padx=5, pady=6)

    #Exibir livros emprestados
    img_livros_emprestados = Image.open('icons/cart.png')
    img_livros_emprestados = img_livros_emprestados.resize((18,18))
    img_livros_emprestados = ImageTk.PhotoImage(img_livros_emprestados)

    b_livros_emprestados = Button(frameEsquerda, image=img_livros_emprestados, compound=LEFT, anchor=NW, text=" Livros emprestados", bg= co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_livros_emprestados.grid(row=6, column=0, sticky=NSEW, padx=5, pady=6)
    



    janela.mainloop()

import sqlite3

#Conexao com banco de dados
conn = sqlite3.connect("dados.db")

#tabela de livros 

conn.execute('CREATE TABLE livros(\
                id INTEGER PRIMARY KEY AUTOINCREMENT,\
                titulo TEXT,\
                autor TEXT,\
                editora TEXT,\
                ano_publicacao INTEGER,\
                isbn TEXT)')

#tabela de usuarios 

conn.execute('CREATE TABLE usuarios(\
                id INTEGER PRIMARY KEY AUTOINCREMENT,\
                nome TEXT,\
                sobrenome TEXT,\
                endereco TEXT,\
                email TEXT,\
                telefone TEXT)')

# tabela de emprestimo

conn.execute('CREATE TABLE emprestimos(\
                id INTEGER PRIMARY KEY AUTOINCREMENT,\
                id_livro INTEGER,\
                id_usuario INTEGER,\
                data_emprestimo TEXT,\
                data_devolucao TEXT,\
                FOREIGN KEY(id_livro) REFERENCES livros(id),\
                FOREIGN KEY(id_usuario) REFERENCES usuarios(id))')
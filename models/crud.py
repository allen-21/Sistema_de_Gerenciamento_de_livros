import sqlite3

# conectar com o banco de dados
def connect():
    conn = sqlite3.connect("dados.db")
    return conn

# inserir livro
def insert_book(titulo, autor, editora, ano_publicacao, isbn):
    conn = connect()
    conn.execute("INSERT INTO livros(titulo, autor, editora, ano_publicacao, isbn)\
                  VALUES (?, ?, ?, ?, ?)",(titulo, autor, editora, ano_publicacao, isbn))
    conn.commit()
    conn.close()

#Listar os livros
def listar_livros():
    conn = connect()
    livros = conn.execute("SELECT * FROM livros").fetchall()
    conn.close()

    if not livros:
        print("Nemhum livro encontrado na biblioteca")
        return
    print("Livros na biblioteca: ")
    for livro in livros:
        print(f"ID: {livro[0]}")
        print(f"Titulo: {livro[1]}")
        print(f"Autor: {livro[2]}")
        print(f"Editora: {livro[3]}")
        print(f"Ano da Publicacao: {livro[4]}")
        print(f"Isbn: {livro[5]}")
        print("\n")

# Inserir usuarios 
def insert_user(nome, sobrenome, endereco, email, telefone):
    conn = connect()
    conn.execute("INSERT INTO usuarios(nome, sobrenome, endereco, email, telefone)\
                  VALUES (?, ?, ?, ?, ?)",(nome, sobrenome, endereco, email, telefone))
    conn.commit()
    conn.close()

# Inserir emprestimos
def insert_loan(id_livro, id_usuario, data_emprestimo, data_devolucao):
    conn = connect()
    conn.execute("INSERT INTO emprestimo(id_livro, id_usuario, data_emprestimo, data_devolucao)\
                  VALUES (?, ?, ?, ?)",(id_livro, id_usuario, data_emprestimo, data_devolucao))
    conn.commit()
    conn.close()

#Exibir emprestimos 
def get_books_on_lean():
    conn = connect()
    result = conn.execute("SELECT livros.titulo, usuarios.nome, usuarios.sobrenome, emprestimo.data_emprestimo, emprestimo.data_devolucao\
                           FROM livros\
                          INNER JOIN emprestimos ON livros.id = emprstimos.id_livro\
                          INNER JOIN usuarios ON usuarios.id = emprestimos.id_usuario\
                          WHERE emprstimos.data_devolucao IS NULL").fetchall()
    conn.close()
    return result
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
    return livros

# Inserir usuarios 
def insert_user(nome, sobrenome, endereco, email, telefone):
    conn = connect()
    conn.execute("INSERT INTO usuarios(nome, sobrenome, endereco, email, telefone)\
                  VALUES (?, ?, ?, ?, ?)",(nome, sobrenome, endereco, email, telefone))
    conn.commit()
    conn.close()

# Exibir usuarios 
def get_users():
    conn = connect()
    usuarios = conn.execute("SELECT* FROM usuarios").fetchall()
    conn.close()
    return usuarios

    
# Inserir emprestimos
def insert_loan(id_livro, id_usuario, data_emprestimo, data_devolucao):
    conn = connect()
    conn.execute("INSERT INTO emprestimos(id_livro, id_usuario, data_emprestimo, data_devolucao)\
                  VALUES (?, ?, ?, ?)",(id_livro, id_usuario, data_emprestimo, data_devolucao))
    conn.commit()
    conn.close()


#Devolucao do livro

def update_loan_return_date(id_emprestimo, data_devolucao):
    conn = connect()
    conn.execute(
        "UPDATE emprestimos SET data_devolucao = ? WHERE id = ?", 
        (data_devolucao, id_emprestimo)
    )
    conn.commit()
    conn.close()

#Exibir emprestimos 
def get_books_on_lean():
    conn = connect()
    result = conn.execute(
        "SELECT emprestimos.id, livros.titulo, \
                usuarios.nome || ' ' || usuarios.sobrenome AS nome_completo, \
                emprestimos.data_emprestimo, emprestimos.data_devolucao \
         FROM livros \
         INNER JOIN emprestimos ON livros.id = emprestimos.id_livro \
         INNER JOIN usuarios ON usuarios.id = emprestimos.id_usuario \
         WHERE emprestimos.data_devolucao IS NULL"
    ).fetchall()
    conn.close()
    return result



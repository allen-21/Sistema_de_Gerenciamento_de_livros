import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.crud import insert_book,insert_user, listar_livros

#crud do livro
#insert_book("Python", "Anibal", "Plurar", 2020, "484as845648" )

listar_livros()


#crud do usuario
#insert_user("Valter", "Muchanga", "Malhazine", "valteranibal1@gmail.com", "8445484564845" )
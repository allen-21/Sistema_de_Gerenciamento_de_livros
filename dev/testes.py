import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.crud import *

#crud do livro
'insert_book("Python", "Anibal", "Plurar", 2020, "484as845648" )'

'listar_livros()'


#crud do usuario
'insert_user("Valter", "Muchanga", "Malhazine", "valteranibal1@gmail.com", "8445484564845" )'
'get_users()'


#crud do empretimo
'insert_loan(1,1,"2025-07-21", None)'
'update_loan_return_date(1, "2025-07-22")'
'print(get_books_on_lean())'
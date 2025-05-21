import sqlite3
def conectar ():
    return sqlite3.connect ("libros.db")

def agregar ():
    genero=input("genero:")
    anio=input("anio:")
    autor=input("autor:")
    titulo=input("titulo:")
    with conectar () as conn:
        conn.execute('''INSERT INTO libros (genero,anio,autor,titulo) VALUES ''')
    print("Libro agregado")

def modificar():
    id=input("ID del libro a modificar: ")
    genero=input ("nuevo genero:" )
    anio=int(input("nuevo anio:" ))
    autor=input("nuevo autor: ")
    titulo=input("nuevo titulo:")
    with conectar () as conn:
        conn.execute ("UPDATE libros SET genero=romance, anio=2012, autor=stephen king, titulo=el payaso del mal WHERE id")
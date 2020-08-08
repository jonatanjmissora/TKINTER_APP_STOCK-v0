import sqlite3

#============= CONSTANTES =================
#datos = [(15, 20, 17, 15, 18), (3, 4, 2, 3, 2), (5, 13, 5, 9, 5),
#         (2, 10, 8, 2, 8), (1, 39, 6, 7, 1), (5, 10, 8, 5, 3),
#         (5, 20, 7, 5, 8), (3, 14, 2, 13, 2), (5, 13, 5, 9, 5),
#         (2, 10, 8, 2, 8), (1, 39, 6, 7, 1), (5, 10, 8, 5, 3),
#         (5, 20, 7, 5, 8), (3, 14, 2, 3, 2), (5, 13, 5, 9, 5),
#         (2, 10, 8, 2, 8), (1, 39, 6, 7, 11), (5, 10, 8, 5, 3),
#         (5, 20, 7, 5, 8), (3, 14, 2, 3, 2), (5, 13, 5, 19, 5),
#         (2, 10, 8, 2, 8),]

talles = [40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60]

#============= FUNCIONES DATOS ===============  

def datos_txt():
  correcion_espacio = " "
  string_relleno = []
  for i in range(1, 23):
    # obtengo el renglon i-esimo de la tabla
    row = obtener_uno(i)
    
    #cargo el primer dato del renglon
    num = str(row[0])
    if len(num) > 1:
        correcion_espacio = ""
    else:
        correcion_espacio = " "
    renglon = "     " + correcion_espacio + num
    
    #cargo el resto de los datos del renglon
    for j in range(1, 5):
      num = str(row[j])
      if len(num) > 1:
        correcion_espacio = ""
      else:
        correcion_espacio = "  "
      renglon += " "*9 + correcion_espacio + num
    renglon += "\n"
    #cargo el renglon ya en formato txt
    string_relleno.append(renglon)
  
  return string_relleno                  

def modificar_datos(talle, li1, li2):
  global datos
  indice = talles.index(talle)*2
  datos[indice]=li1
  datos[indice+1]=li2
  
#==============================================
#============= SQLITE3 ========================
#==============================================

# crear una tabla
def crear_tabla():
  conn = sqlite3.connect("datos_db.db")
  c = conn.cursor()

  c.execute("""CREATE TABLE datos_tb (
        jean int,
        blue int,
        gris int,
        negro int,
        oxido int,)
        """)
  conn.commit()
  conn.close()

# cargar todos los datos de la tabla
def insert_todos(lista):
  conn = sqlite3.connect("datos_db.db")
  c = conn.cursor()
  c.executemany("INSERT INTO datos_tb VALUES (?,?,?,?,?)", lista)
  conn.commit()
  conn.close()

# mostrar todos los datos
def mostrar_todos():
  conn = sqlite3.connect("datos_db.db")
  c = conn.cursor()
  c.execute("SELECT * FROM datos_tb")
  [print(row) for row in c.fetchall()]
  conn.commit()
  conn.close()

def obtener_uno(indice):
  conn = sqlite3.connect("datos_db.db")
  c = conn.cursor()
  c.execute("SELECT * FROM datos_tb WHERE rowid=?", (indice, ))
  row = c.fetchone()
  conn.commit()
  conn.close()
  return row

#crear_tabla()
#insert_todos(datos)
#mostrar_todos()

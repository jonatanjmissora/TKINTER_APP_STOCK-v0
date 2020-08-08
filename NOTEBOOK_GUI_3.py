import PINTAR
import DATOS
import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import *

win = tk.Tk()
win.geometry("500x800+10+0")
note = ttk.Notebook(win, width=425, height=660, padding=3)
note.pack()

# ================= CONSTANTES ====================================
fnt12 = ("Arial", 12, "bold")
fnt10 = ("Arial", 10, "bold")
fabricantes=["TOXICO", "BLESS", "GENTE J", "TEXTIL M"]
talles = [40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60]

# ================= FUNCIONES ===================================
def seleccion_talle(event):
	talle_txt.set(combo3.get())

def cambiar_datos():
	cambio1=(en1.get(), en2.get(), en3.get(), en4.get(), en5.get())
	cambio2=(en6.get(), en7.get(), en8.get(), en9.get(), en10.get())
	DATOS.modificar_datos(int(talle_txt.get()), cambio1, cambio2)
	imprimir_datos()
	
	# borrar entries
	en1.delete(0, END)
	en2.delete(0, END)
	en3.delete(0, END)
	en4.delete(0, END)
	en5.delete(0, END)
	en6.delete(0, END)
	en7.delete(0, END)
	en8.delete(0, END)
	en9.delete(0, END)
	en10.delete(0, END)
	
def seleccion_fabrica(event):
	pass

def imprimir_datos():
	datos=DATOS.datos_txt()
	list1=Text(f14, font=("Arial", 14))
	list1.place(x=80, y=0)
	for i in range(0, 22):
		list1.insert(str(i+1)+".0", datos[i])
	list1.configure(state='disabled')
	
	# ============= F14 "SEPARADORES" ===============================================
	for i in range(len(talles)):
		Frame(f14, height=2, bd=1, bg="light grey", relief=SUNKEN).grid(row=2*i+1, column=3, ipadx=200, sticky=N)
		Frame(f14, height=3, bd=1, bg="black", relief=SUNKEN).grid(row=2*i+2, column=3, ipadx=200, sticky=N)
	for i in range(4):
		sep=ttk.Separator(f14, orient=VERTICAL).place(x=148+i*69, y=0, height=500)

# =============================================================
# ==================== FABRICA ================================
# =============================================================

#creacion de etiqueta "FABRICA"
fabrica = Frame(note, bd=2, relief="sunken")
note.add(fabrica, text="FABRICA")

#============= FRAMES 1-4 CREAR ============================

# contiene las fabricas
f11 = Frame(fabrica, padx=10, pady=20)
f11.pack(fill=X)

# contiene los checkboxes
f12 = Frame(fabrica)
f12.pack(fill=X)

# contiene el titulo de la lista
f13 = Frame(fabrica, height=515, width=500)
f13.place(x=0, y=140)

# contiene la lista
f14 = Frame(f13, width=394, height=500)
f14.place(x=0, y=27, relwidth=1)


#============= F11 "FABRICAS" ==================

Label(f11, text="FABRICA:", font=fnt12).pack(side=LEFT)
combo=Combobox(f11, values=fabricantes, width=10, state="readonly", font=fnt12)
combo.pack(side=LEFT)                             
combo.current(0)                
combo.bind("<<ComboboxSelected>>", seleccion_fabrica)
combo.bind("<Return>", seleccion_fabrica) 

#============= F12 "CHECKBUTTONS" =========================

var_c_rotura = BooleanVar()
var_s_rotura = BooleanVar()
var_jean = BooleanVar()
var_blue = BooleanVar()
var_gris = BooleanVar()
var_negro = BooleanVar()
var_oxido = BooleanVar()
ck_c_rotura = Checkbutton(f12, text="c/rotura", justify=LEFT, variable=var_c_rotura,
							command=lambda:PINTAR.c_rotura(f14, var_c_rotura.get()), font=fnt12)
ck_s_rotura = Checkbutton(f12, text="s/rotura", justify=LEFT, variable=var_s_rotura, 
							command=lambda:PINTAR.s_rotura(f14, var_s_rotura.get()), font=fnt12)
ck_jean = Checkbutton(f12, text="jean", justify=LEFT, variable=var_jean, 
							command=lambda:PINTAR.jean(f14, var_jean.get()), font=fnt12)
ck_blue = Checkbutton(f12, text="blueblack", justify=LEFT, variable=var_blue, 
							command=lambda:PINTAR.blue(f14, var_blue.get()), font=fnt12)
ck_gris = Checkbutton(f12, text="gris", justify=LEFT, variable=var_gris, 
							command=lambda:PINTAR.gris(f14, var_gris.get()), font=fnt12)
ck_negro = Checkbutton(f12, text="negro", justify=LEFT, variable=var_negro, 
							command=lambda:PINTAR.negro(f14, var_negro.get()), font=fnt12)
ck_oxido = Checkbutton(f12, text="oxido", justify=LEFT, variable=var_oxido, 
							command=lambda:PINTAR.oxido(f14, var_oxido.get()), font=fnt12)

ck_c_rotura.select()
ck_s_rotura.select()
ck_jean.select()
ck_blue.select()
ck_gris.select()
ck_negro.select()
ck_oxido.select()

ck_c_rotura.grid(row=0, column=0, sticky=W, padx=5)
ck_s_rotura.grid(row=1, column=0, sticky=W, padx=5)
ck_jean.grid(row=0, column=1, sticky=W, padx=5)  
ck_blue.grid(row=1, column=1, sticky=W, padx=5)  
ck_gris.grid(row=0, column=2, sticky=W, padx=5)  
ck_negro.grid(row=1, column=2, sticky=W, padx=5)
ck_oxido.grid(row=0, column=3, sticky=W, padx=5) 

#============== F13 "TITULO LISTADO" ===========================

Label(f13, text ="TALLE             JEAN         BLUE        GRIS        NEGRO      OXIDO    ", font=fnt10).place(x=5, y=5)
Frame(f13, height=2, bd=1, bg="grey", relief=SUNKEN).place(x=0, y=25, relwidth=1)	

# ============= F14 "TALLES" ======================================
for i in range(len(talles)):
	Label(f14, text=talles[i], font=("Arial", 25, "bold"), relief=GROOVE).grid(row=2*i, column=0, rowspan=2)
	Label(f14, text="c/rot", width=4, font=("Arial", 10, "bold"), relief=GROOVE).grid(row=2*i, column=1)		
	Label(f14, text="s/rot", width=4, font=("Arial", 10, "bold"), relief=GROOVE).grid(row=2*i+1, column=1)

# ============= F4 "DATOS" ======================================
imprimir_datos()



# ==============================================================
# ==================== ARTICULO ================================
# ==============================================================
fr2 = Frame(note, bd=2, relief="sunken")
note.add(fr2, text="ARTICULO")
lab2 = Label(fr2, text="ARTICULO").grid()
#
#
#
# =============================================================
# ==================== CARGAR =================================
# =============================================================
cargar = Frame(note, bd=2, relief="sunken")
note.add(cargar, text="CARGAR")
        
#============= FRAMES 1 al 4 ============================

# contiene las fabricas
f31 = Frame(cargar, padx=10, pady=20)
f31.pack(fill=X)

# contiene el talle
f32 = Frame(cargar)
f32.pack(fill=X)

#contiene el titulo de la lista a cargar
f33 = Frame(cargar, height=35, width=500)
f33.place(x=0, y=110)

# contiene la lista a cargar
f34 = Frame(cargar, width=394, height=500)
f34.place(x=0, y=140, relwidth=1)

#============= F31 "FABRICAS" ============================
Label(f31, text="FABRICA:", font=fnt12).pack(side=LEFT)

combo2=Combobox(f31, values=fabricantes, width=10, state="readonly", font=fnt12)
combo2.pack(side=LEFT)                             
combo2.current(0)                
combo2.bind("<<ComboboxSelected>>", seleccion_fabrica)
combo2.bind("<Return>", seleccion_fabrica) 

#============== F32 "TALLE A CARGAR" ===========================
Label(f32, text="TALLE:", font=fnt12).pack(side=LEFT)
talles=["40", "42", "44", "46", "48", "50", "52", "54", "56", "58", "60"]
combo3=Combobox(f32, values=talles, width=5, state="readonly", font=fnt12)
combo3.pack(side=LEFT)                             
combo3.current(0)                
combo3.bind("<<ComboboxSelected>>", seleccion_talle)
combo3.bind("<Return>", seleccion_talle) 

#============== F33 "TITULO LISTADO" ===========================

Label(f33, text ="TALLE           JEAN      BLUE        GRIS      NEGRO     OXIDO    ", font=fnt10).place(x=5, y=5)
Frame(f33, height=2, bd=1, bg="grey", relief=SUNKEN).place(x=0, y=25, relwidth=1)	

# ============= F34 "TALLE A CARGAR" =============================
talle_txt = StringVar()
talle_txt.set("40")
talle_lb=Label(f34, textvariable=talle_txt, font=("Arial", 25, "bold"), relief=GROOVE)
talle_lb.grid(row=0, column=0, rowspan=2)
Label(f34, text="c/rot", width=4, font=("Arial", 10, "bold"), relief=GROOVE).grid(row=0, column=1)		
Label(f34, text="s/rot", width=4, font=("Arial", 10, "bold"), relief=GROOVE).grid(row=1, column=1)

# ============= F34 "DATOS A CARGAR" =============================
en1=Entry(f34, width=8, justify=CENTER)
en1.grid(row=0, column=2)
en2=Entry(f34, width=8, justify=CENTER)
en2.grid(row=0, column=3)
en3=Entry(f34, width=8, justify=CENTER)
en3.grid(row=0, column=4)
en4=Entry(f34, width=9, justify=CENTER)
en4.grid(row=0, column=5)
en5=Entry(f34, width=9, justify=CENTER)
en5.grid(row=0, column=6)
en6=Entry(f34, width=8, justify=CENTER)
en6.grid(row=1, column=2)
en7=Entry(f34, width=8, justify=CENTER)
en7.grid(row=1, column=3)
en8=Entry(f34, width=8, justify=CENTER)
en8.grid(row=1, column=4)
en9=Entry(f34, width=9, justify=CENTER)
en9.grid(row=1, column=5)
en10=Entry(f34, width=9, justify=CENTER)
en10.grid(row=1, column=6)

Label(f34).grid(row=2, column=0)
but1=Button(f34, text="CARGAR", command=cambiar_datos)
but1.grid(row=3, column=3)


tk.mainloop()

import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import *

win = tk.Tk()

# ================= CONSTANTES ====================================
fnt12 = ("Arial", 12, "bold")
fnt10 = ("Arial", 10, "bold")
c_roturas = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
string_relleno = [(" "*5 + "5" + " "*9 + "8" + " "*9 + "10" + " "*9 + "7" + " "*(9+2) + "3" + "\n"),
				  (" "*5 + "5" + " "*9 + "8" + " "*9 + "10" + " "*9 + "7" + " "*(9+2) + "3" + "\n"),
				  (" "*5 + "5" + " "*9 + "8" + " "*9 + "10" + " "*9 + "7" + " "*(9+2) + "3" + "\n"),
				  (" "*5 + "5" + " "*9 + "8" + " "*9 + "10" + " "*9 + "7" + " "*(9+2) + "3" + "\n"),
				  (" "*5 + "5" + " "*9 + "8" + " "*9 + "10" + " "*9 + "7" + " "*(9+2) + "3" + "\n"),
				  (" "*5 + "5" + " "*9 + "8" + " "*9 + "10" + " "*9 + "7" + " "*(9+2) + "3" + "\n"),
				  (" "*5 + "5" + " "*9 + "8" + " "*9 + "10" + " "*9 + "7" + " "*(9+2) + "3" + "\n"),
				  (" "*5 + "5" + " "*9 + "8" + " "*9 + "10" + " "*9 + "7" + " "*(9+2) + "3" + "\n"),
				  (" "*5 + "5" + " "*9 + "8" + " "*9 + "10" + " "*9 + "7" + " "*(9+2) + "3" + "\n"),
				  (" "*5 + "5" + " "*9 + "8" + " "*9 + "10" + " "*9 + "7" + " "*(9+2) + "3" + "\n"),	
				  (" "*5 + "5" + " "*9 + "8" + " "*9 + "10" + " "*9 + "7" + " "*(9+2) + "3" + "\n"),
				  (" "*5 + "5" + " "*9 + "8" + " "*9 + "10" + " "*9 + "7" + " "*(9+2) + "3" + "\n"),
				  (" "*5 + "5" + " "*9 + "8" + " "*9 + "10" + " "*9 + "7" + " "*(9+2) + "3" + "\n"),
				  (" "*5 + "5" + " "*9 + "8" + " "*9 + "10" + " "*9 + "7" + " "*(9+2) + "3" + "\n"),
				  (" "*5 + "5" + " "*9 + "8" + " "*9 + "10" + " "*9 + "7" + " "*(9+2) + "3" + "\n"),
				  (" "*5 + "5" + " "*9 + "8" + " "*9 + "10" + " "*9 + "7" + " "*(9+2) + "3" + "\n"),
				  (" "*5 + "5" + " "*9 + "8" + " "*9 + "10" + " "*9 + "7" + " "*(9+2) + "3" + "\n"),
				  (" "*5 + "5" + " "*9 + "8" + " "*9 + "10" + " "*9 + "7" + " "*(9+2) + "3" + "\n"),
				  (" "*5 + "5" + " "*9 + "8" + " "*9 + "10" + " "*9 + "7" + " "*(9+2) + "3" + "\n"),
				  (" "*5 + "5" + " "*9 + "8" + " "*9 + "10" + " "*9 + "7" + " "*(9+2) + "3" + "\n"),	
				  (" "*5 + "5" + " "*9 + "8" + " "*9 + "10" + " "*9 + "7" + " "*(9+2) + "3" + "\n"),
				  (" "*5 + "5" + " "*9 + "8" + " "*9 + "10" + " "*9 + "7" + " "*(9+2) + "3" + "\n"),]




def c_rotura():
	global lb_gris_c_roturas1, lb_gris_c_roturas2, lb_gris_c_roturas3, lb_gris_c_roturas4, lb_gris_c_roturas5, lb_gris_c_roturas6, lb_gris_c_roturas7, lb_gris_c_roturas8
	global lb_gris_c_roturas9, lb_gris_c_roturas10, lb_gris_c_roturas11
	if not var.get():
		lb_gris_c_roturas1=Label(f4, text=" ", bg="light grey", width=100, height=1)
		lb_gris_c_roturas1.place(x=80, y=0)
		lb_gris_c_roturas2=Label(f4, text=" ", bg="light grey", width=100, height=1)
		lb_gris_c_roturas2.place(x=80, y=44)
		lb_gris_c_roturas3=Label(f4, text=" ", bg="light grey", width=100, height=1)
		lb_gris_c_roturas3.place(x=80, y=88)
		lb_gris_c_roturas4=Label(f4, text=" ", bg="light grey", width=100, height=1)
		lb_gris_c_roturas4.place(x=80, y=132)
		lb_gris_c_roturas5=Label(f4, text=" ", bg="light grey", width=100, height=1)
		lb_gris_c_roturas5.place(x=80, y=176)
		lb_gris_c_roturas6=Label(f4, text=" ", bg="light grey", width=100, height=1)
		lb_gris_c_roturas6.place(x=80, y=220)
		lb_gris_c_roturas7=Label(f4, text=" ", bg="light grey", width=100, height=1)
		lb_gris_c_roturas7.place(x=80, y=264)
		lb_gris_c_roturas8=Label(f4, text=" ", bg="light grey", width=100, height=1)
		lb_gris_c_roturas8.place(x=80, y=308)
		lb_gris_c_roturas9=Label(f4, text=" ", bg="light grey", width=100, height=1)
		lb_gris_c_roturas9.place(x=80, y=352)
		lb_gris_c_roturas10=Label(f4, text=" ", bg="light grey", width=100, height=1)
		lb_gris_c_roturas10.place(x=80, y=396)
		lb_gris_c_roturas11=Label(f4, text=" ", bg="light grey", width=100, height=1)
		lb_gris_c_roturas11.place(x=80, y=440)
	else:
		lb_gris_c_roturas1.destroy()
		lb_gris_c_roturas2.destroy()
		lb_gris_c_roturas3.destroy()
		lb_gris_c_roturas4.destroy()
		lb_gris_c_roturas5.destroy()
		lb_gris_c_roturas6.destroy()
		lb_gris_c_roturas7.destroy()
		lb_gris_c_roturas8.destroy()
		lb_gris_c_roturas9.destroy()
		lb_gris_c_roturas10.destroy()
		lb_gris_c_roturas11.destroy()

def s_rotura():
	pass

def jean():
	pass

def blueblack():
	pass

def gris():
	pass

def negro():
	pass

def oxido():
	pass

def seleccion(event):
	pass

note = ttk.Notebook(win, width=400, height=660, padding=3)
note.pack()

# ============== FABRICA y CHECKBOXES =========================
# =============================================================

#creacion de etiqueta "FABRICA"
fabrica = Frame(note, bd=2, relief="sunken")
note.add(fabrica, text="FABRICA")

#============= FRAME 1 ("FABRICA + COMBOBOX") ============================
f1 = Frame(fabrica, padx=10, pady=20)
f1.pack(fill=X)

Label(f1, text="FABRICA:", font=fnt12).pack(side=LEFT)

fabricantes=["TOXICO", "BLESS", "GENTE J", "TEXTIL M"]
combo=Combobox(f1, values=fabricantes, width=10, state="readonly", font=fnt12)
combo.pack(side=LEFT)                             
combo.current(0)                
combo.bind("<<ComboboxSelected>>", seleccion)
combo.bind("<Return>", seleccion) 

#============= FRAME 2 "CHECKBUTTONS" =========================
f2 = Frame(fabrica)
f2.pack(fill=X)
var = BooleanVar()
ck_c_rotura = Checkbutton(f2, text="c/rotura", justify=LEFT, variable=var, command=c_rotura, font=fnt12)
ck_s_rotura = Checkbutton(f2, text="s/rotura", justify=LEFT, command=s_rotura, font=fnt12)
ck_jean = Checkbutton(f2, text="jean", justify=LEFT, command=jean, font=fnt12)
ck_blueblack = Checkbutton(f2, text="blueblack", justify=LEFT, command=blueblack, font=fnt12)
ck_gris = Checkbutton(f2, text="gris", justify=LEFT, command=gris, font=fnt12)
ck_negro = Checkbutton(f2, text="negro", justify=LEFT, command=negro, font=fnt12)
ck_oxido = Checkbutton(f2, text="oxido", justify=LEFT, command=oxido, font=fnt12)

ck_c_rotura.select()
ck_s_rotura.select()
ck_jean.select()
ck_blueblack.select()
ck_gris.select()
ck_negro.select()
ck_oxido.select()

ck_c_rotura.grid(row=0, column=0, sticky=W, padx=5)
ck_s_rotura.grid(row=1, column=0, sticky=W, padx=5)
ck_jean.grid(row=0, column=1, sticky=W, padx=5)  
ck_blueblack.grid(row=1, column=1, sticky=W, padx=5)  
ck_gris.grid(row=0, column=2, sticky=W, padx=5)  
ck_negro.grid(row=1, column=2, sticky=W, padx=5)
ck_oxido.grid(row=0, column=3, sticky=W, padx=5) 

#============== FRAME 3 "TITULO LISTADO" ===========================
f3 = Frame(fabrica, height=515, width=500)
f3.place(x=0, y=140)

Label(f3, text ="TALLE           JEAN      BLUE        GRIS      NEGRO     OXIDO    ", font=fnt10).place(x=5, y=5)
Frame(f3, height=2, bd=1, bg="grey", relief=SUNKEN).place(x=0, y=25, relwidth=1)	

f4 = Frame(f3, width=394, height=500)
f4.place(x=0, y=27, relwidth=1)

# ============== DATOS ======================================



list1=Text(f4, font=("Arial", 14))
list1.place(x=80, y=0)
for i in range(0, 22):
	list1.insert(str(i+1)+".0", string_relleno[i])

# ========================== talles y roturas ======================================
talles = [40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60]
for i in range(len(talles)):
	Label(f4, text=talles[i], font=("Arial", 25, "bold"), relief=GROOVE).grid(row=2*i, column=0, rowspan=2)
	Label(f4, text="c/rot", width=4, font=("Arial", 10, "bold"), relief=GROOVE).grid(row=2*i, column=1)		
	Label(f4, text="s/rot", width=4, font=("Arial", 10, "bold"), relief=GROOVE).grid(row=2*i+1, column=1)

# ======================== separadores ===============================================
for i in range(len(talles)):
	Frame(f4, height=2, bd=1, bg="light grey", relief=SUNKEN).grid(row=2*i+1, column=3, ipadx=200, sticky=N)
	Frame(f4, height=3, bd=1, bg="black", relief=SUNKEN).grid(row=2*i+2, column=3, ipadx=200, sticky=N)
for i in range(4):
	sep=ttk.Separator(f4, orient=VERTICAL).place(x=140+i*62, y=0, height=500)


#l=Label(f4, text=" ", bg="light grey", width=100, height=1, state="disable")
#l.place(x=80, y=0)
#l.destroy()






# ============== ARTICULO =========================
fr2 = tk.Frame(note, bd=2, relief="sunken")
note.add(fr2, text="ARTICULO")

lab2 = tk.Label(fr2, text="ARTICULO").grid()


# ============== CARGAR =========================
fr3 = tk.Frame(note, bd=2, relief="sunken")
note.add(fr3, text="CARGAR")
        
lab3 = tk.Label(fr3, text="CARGAR").grid()

tk.mainloop()
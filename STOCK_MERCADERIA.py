from tkinter import *

class Ventana():
    def __init__(self, win):
        self.win=win
        self.win.geometry("800x430+1000+100")
        self.win.title("MERCADERIA")
        
        main_frame = Frame(win, bg = "#99ffd6")
        main_frame.pack(fill = X)
        
        #================   FRAMEs   =========================================
        title_frame = Frame(main_frame, bg = "light grey", bd=3, relief=GROOVE)
        title_frame.pack(fill = X, padx = 10, pady = 10)
        title_label = Label(title_frame, text = "STOCK MERCADERIA", font = ("Arial", 20, "bold"), bg = "light grey")
        title_label.pack()

        field_frame = Frame(main_frame, bg = "light grey", bd=2, relief=GROOVE)
        field_frame.pack(fill = X, padx = 10, pady = 10)

        button_frame = Frame(main_frame, bg = "light grey", bd=1, relief=GROOVE)
        button_frame.pack(fill = X, padx = 10, pady = 10)
        
        #================   LABELs  =========================================
        fabrica_lab = Label(field_frame, text = "fabrica: ", font = ("Arial", 15, "bold"), bg = "light grey")
        fabrica_lab.grid(row=0, column=0, sticky = W, padx=5, pady=5)
        art_lab = Label(field_frame, text = "articulo: ", font = ("Arial", 15, "bold"), bg = "light grey")
        art_lab.grid(row=1, column=0, sticky = W, padx=5, pady=5)
        desc_lab = Label(field_frame, text = "descrip: ", font = ("Arial", 15, "bold"), bg = "light grey")
        desc_lab.grid(row=2, column=0, sticky = W, padx=5, pady=5)
        cant_lab = Label(field_frame, text = "cantidad: ", font = ("Arial", 15, "bold"), bg = "light grey")
        cant_lab.grid(row=3, column=0, sticky = W, padx=5, pady=5)
        colores_lab = Label(field_frame, text = "colores: ", font = ("Arial", 15, "bold"), bg = "light grey")
        colores_lab.grid(row=4, column=0, sticky = W, padx=5, pady=5)
        talles_lab = Label(field_frame, text = "talles: ", font = ("Arial", 15, "bold"), bg = "light grey")
        talles_lab.grid(row=5, column=0, sticky = W, padx=5, pady=5)
        precio_lab = Label(field_frame, text = "precio: ", font = ("Arial", 15, "bold"), bg = "light grey")
        precio_lab.grid(row=6, column=0, sticky = W, padx=5, pady=5)

        #================   ENTRYs  =========================================
        fabrica_ent = Entry(field_frame, width = 20, font = ("Arial", 15, "bold"))
        fabrica_ent.grid(row=0, column=1)
        art_ent = Entry(field_frame, width = 20, font = ("Arial", 15, "bold"))
        art_ent.grid(row=1, column=1)
        desc_ent = Entry(field_frame, width = 20, font = ("Arial", 15, "bold"))
        desc_ent.grid(row=2, column=1)
        cant_ent = Entry(field_frame, width = 20, font = ("Arial", 15, "bold"))
        cant_ent.grid(row=3, column=1)
        colores_ent = Entry(field_frame, width = 20, font = ("Arial", 15, "bold"))
        colores_ent.grid(row=4, column=1)
        talles_ent = Entry(field_frame, width = 20, font = ("Arial", 15, "bold"))
        talles_ent.grid(row=5, column=1)
        precio_ent = Entry(field_frame, width = 20, font = ("Arial", 15, "bold"))
        precio_ent.grid(row=6, column=1)

        #==================  BUTTONs  ==========================================
        guardar_bt = Button(button_frame, text = "GUARDAR")
        guardar_bt.pack(side=LEFT, padx=5, pady=5)
        borrar_bt = Button(button_frame, text = "BORRAR")
        borrar_bt.pack(side=LEFT, padx=5, pady=5)
        listar_bt = Button(button_frame, text = "LISTAR")
        listar_bt.pack(side=LEFT, padx=5, pady=5)
        cambiar_bt = Button(button_frame, text = "CAMBIAR")
        cambiar_bt.pack(side=LEFT, padx=5, pady=5)
        cerrar_bt = Button(button_frame, text = "CERRAR")
        cerrar_bt.pack(side=RIGHT, padx=5, pady=5)
        
root=Tk()
v1 = Ventana(root)
root.mainloop()
from tkinter import *
from tkinter import font

class Ventana():
    
    def __init__(self, win):
        main_bg = "cadet blue"
        label_bg = "light grey"
        fnt = ("Arial", 15, "bold")

        self.win=win
        self.win.geometry("800x515+100+50")
        self.win.title("MERCADERIA")
        
        main_frame = Frame(win, bg = main_bg)
        main_frame.pack(fill = X)
        
        #================   FRAMEs   =========================================
        title_frame = Frame(main_frame, bg = label_bg)
        title_frame.pack(fill = X, padx = 10, pady = 10)
        title_label = Label(title_frame, text = "STOCK MERCADERIA", font = ("Arial", 20, "bold"), bg = label_bg)
        title_label.pack(side=TOP)

        field_frame = Frame(main_frame, bg = label_bg)
        field_frame.pack(fill = X, padx = 10, pady = 10, )

        button_frame = Frame(main_frame, bg = label_bg)
        button_frame.pack(fill = X, padx = 10, pady = 10)

        list_frame = Frame(main_frame, bg = label_bg)
        list_frame.pack(fill = X, padx = 10, pady = 10)
        
        #================   LABELs  =========================================
        fabrica_lab = Label(field_frame, text = "fabrica: ", font = fnt, bg = label_bg)
        fabrica_lab.grid(row=0, column=0, sticky = E, padx=5, pady=5)
        art_lab = Label(field_frame, text = "articulo: ", font = fnt, bg = label_bg)
        art_lab.grid(row=1, column=0, sticky = E, padx=5, pady=5)
        desc_lab = Label(field_frame, text = "descrip: ", font = fnt, bg = label_bg)
        desc_lab.grid(row=2, column=0, sticky = E, padx=5, pady=5)
        cant_lab = Label(field_frame, text = "cantidad: ", font = fnt, bg = label_bg)
        cant_lab.grid(row=3, column=0, sticky = E, padx=5, pady=5)
        colores_lab = Label(field_frame, text = "colores: ", font = fnt, bg = label_bg)
        colores_lab.grid(row=0, column=3, sticky = E, padx=5, pady=5)
        talles_lab = Label(field_frame, text = "talles: ", font = fnt, bg = label_bg)
        talles_lab.grid(row=1, column=3, sticky = E, padx=5, pady=5)
        precio_lab = Label(field_frame, text = "precio: ", font = fnt, bg = label_bg)
        precio_lab.grid(row=2, column=3, sticky = E, padx=5, pady=5)

        #================   ENTRYs  =========================================
        fabr_var = StringVar()
        art_var = StringVar()
        desc_var = StringVar()
        cant_var = StringVar()
        col_var = StringVar()
        tall_var = StringVar()
        prec_var = StringVar()
        fabrica_ent = Entry(field_frame, textvariable = fabr_var , width = 20, font = fnt)
        fabrica_ent.grid(row=0, column=1)
        art_ent = Entry(field_frame, textvariable = art_var , width = 20, font = fnt)
        art_ent.grid(row=1, column=1)
        desc_ent = Entry(field_frame, textvariable = desc_var , width = 20, font = fnt)
        desc_ent.grid(row=2, column=1)
        cant_ent = Entry(field_frame, textvariable = cant_var , width = 20, font = fnt)
        cant_ent.grid(row=3, column=1)
        colores_ent = Entry(field_frame, textvariable = col_var , width = 20, font = fnt)
        colores_ent.grid(row=0, column=4)
        talles_ent = Entry(field_frame, textvariable = tall_var , width = 20, font = fnt)
        talles_ent.grid(row=1, column=4)
        precio_ent = Entry(field_frame, textvariable = prec_var , width = 20, font = fnt)
        precio_ent.grid(row=2, column=4)

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
        
        #==================  LIST  ==========================================
        fnt_lst = ("Arial", 10, "bold")
        wd_list = 12
        list_lb_txt = ("CANTIDAD", "ARTICULO", "DESCRIP", "TALLES", "COLORES", "FABRICA", "PRECIO")
        for x in range(len(list_lb_txt)):
            L=Label(list_frame, text = list_lb_txt[x], width=wd_list, bg = "light grey", font = fnt_lst)
            L.grid(row=0, column=x)
            f=font.Font(L, L.cget("font"))
            f.configure(weight="bold", size=12, underline=True)
            L.configure(font=f)
      
        lista1 = ("23", "330", "jean clasico", "38-48", "jean", "Bless", "2100")
        lista2 = ("40", "20-05", "jean elastiz", "38-48", "blue, gris", "Toxico", "1990")
        lista3 = ("12", "20-05", "jean elastiz", "38-48", "blue, gris", "Toxico", "1990")
        lista4 = ("67", "20-05", "jean elastiz", "38-48", "blue, gris", "Toxico", "1990")

        self.listas(list_frame, lista1, 1)
        self.listas(list_frame, lista2, 2)

        
    def listas(self, fr, lis, r):
        for x in range(len(lis)):
            Label(fr, text = lis[x], width=10, bg = "light grey", font = ("Arial", 12)).grid(row=r, column=x)




root=Tk()
v1 = Ventana(root)
root.mainloop()
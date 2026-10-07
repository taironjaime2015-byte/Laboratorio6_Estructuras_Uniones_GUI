# This code is generated using PyUIbuilder: https://pyuibuilder.com

import os
import tkinter as tk
from tkinter import ttk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


main = tk.Tk()
main.title("Main Window")
main.config(bg="#E4E2E2")
main.geometry("714x485")
main.update_idletasks()

geometryX = 0
geometryY = 0

main.geometry("+%d+%d"%(geometryX, geometryY))


style = ttk.Style(main)
style.theme_use("clam")

menu = tk.Menu(main)
main.config(menu=menu)
menu_0 = tk.Menu(menu, tearoff=0)
menu_0.add_command(label="New", command=lambda: print("New clicked"))
menu_0.add_command(label="Open", command=lambda: print("Open clicked"))
menu.add_cascade(label="File", menu=menu_0)
menu_1 = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=menu_1)
menu_2 = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="New Item", menu=menu_2)

style.configure("nombre.TLabel", background="#E4E2E2", foreground="#000", anchor="center")
nombre = ttk.Label(master=main, text="Nombre:", style="nombre.TLabel")
nombre.configure(anchor="center")
nombre.place(x=38, y=32, width=80, height=40)

style.configure("entry.TEntry", fieldbackground="#fff", foreground="#000")

entry = ttk.Entry(master=main, style="entry.TEntry")
entry.place(x=126, y=44, width=200, height=30)

style.configure("ram.TLabel", background="#E4E2E2", foreground="#000", anchor="center")
ram = ttk.Label(master=main, text="RAM:", style="ram.TLabel")
ram.configure(anchor="center")
ram.place(x=39, y=86, width=80, height=40)

style.configure("entry1.TEntry", fieldbackground="#fff", foreground="#000")

entry1 = ttk.Entry(master=main, style="entry1.TEntry")
entry1.place(x=128, y=94, width=200, height=30)

style.configure("estado.TLabel", background="#E4E2E2", foreground="#000", anchor="center")
estado = ttk.Label(master=main, text="Estado:", style="estado.TLabel")
estado.configure(anchor="center")
estado.place(x=38, y=141, width=80, height=40)

style.configure("entry2.TEntry", fieldbackground="#fff", foreground="#000")

entry2 = ttk.Entry(master=main, style="entry2.TEntry")
entry2.place(x=117, y=149, width=200, height=30)

style.configure("tipo.TLabel", background="#E4E2E2", foreground="#000", anchor="center")
tipo = ttk.Label(master=main, text="Tipo:", style="tipo.TLabel")
tipo.configure(anchor="center")
tipo.place(x=34, y=194, width=80, height=40)

style.configure("entry3.TEntry", fieldbackground="#fff", foreground="#000")

entry3 = ttk.Entry(master=main, style="entry3.TEntry")
entry3.place(x=111, y=200, width=200, height=30)

style.configure("valor.TLabel", background="#E4E2E2", foreground="#000", anchor="center")
valor = ttk.Label(master=main, text="Valor:", style="valor.TLabel")
valor.configure(anchor="center")
valor.place(x=37, y=248, width=80, height=40)

style.configure("entry4.TEntry", fieldbackground="#fff", foreground="#000")

entry4 = ttk.Entry(master=main, style="entry4.TEntry")
entry4.place(x=109, y=252, width=200, height=30)

style.configure("registrar.TButton", background="#093cb3", foreground="#000", borderwidth=1)
style.map("registrar.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

registrar = ttk.Button(master=main, text="Registrar", style="registrar.TButton")
registrar.place(x=44, y=313, width=80, height=40)

style.configure("resultado.TLabel", background="#E4E2E2", foreground="#000", anchor="center")
resultado = ttk.Label(master=main, text="Resultado", style="resultado.TLabel")
resultado.configure(anchor="w")
resultado.place(x=151, y=314, width=300, height=40)

def registrar_equipo():
    nombre = entry.get()
    ram = entry1.get()
    estado = entry2.get()
    tipo = entry3.get()
    valor = entry4.get()

    equipo = {
        "nombre": nombre,
        "ram": ram,
        "estado": estado
    }
    dato_alternativo = {"tipo": tipo, "valor": valor}

    texto = (
        f"{equipo['nombre']} | {equipo['ram']} GB | {equipo['estado']} | "
        f"{dato_alternativo['tipo']}: {dato_alternativo['valor']}"
    )
    resultado.config(text=texto)

registrar.config(command=registrar_equipo)



main.mainloop()
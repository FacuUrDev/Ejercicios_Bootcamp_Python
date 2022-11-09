from tkinter import *

def seleccionar():
    monitor.config(text="{}".format(opcion.get()))
def reset():
    opcion.set(None)
    monitor.config(text="")

root = Tk()
opcion = StringVar()
opcion.set(None)
Radiobutton(root, text="Fiat", variable=opcion, 
            value='Fiat', command=seleccionar).pack(anchor=W)

Radiobutton(root, text="Toyota", variable=opcion, 
            value='Toyota', command=seleccionar).pack(anchor=W)
Radiobutton(root, text="Renault", variable=opcion,   
            value='Renault', command=seleccionar).pack(anchor=W)
Radiobutton(root, text="Hyundai", variable=opcion,   
            value='Hyndai', command=seleccionar).pack(anchor=W)

monitor = Label(root)
monitor.pack()
Button(root, text="Reiniciar", command=reset).pack()

root.mainloop()

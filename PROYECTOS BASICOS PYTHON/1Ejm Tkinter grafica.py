#debemos siempre importar el TKINDER para traer una ventana y trabajar con representaciones graficas#
from tkinter import *

ventana = Tk()

ventana.title("esta es mi primera interfaz de python")
ventana.geometry('400x300')

Label1=Label(ventana,text="HOLA, ESCRIBE TU NOMBRE", font=("arial bold",10))
Label1.grid(column=0,row=0)

texto1=Entry(ventana,width=20)
texto1.grid(column=0,row=1)

texto2=Entry(ventana,width=20,state="disable")
texto2.grid(column=0,row=2)

texto1.focus()

def accionboton():
    mensaje ="HOLAA "+ texto1.get()
    Label1.configure(text=mensaje)

botton1=Button(ventana,text="click",bg="blue",fg="white",command=accionboton)
botton1.grid(column=0,row=3)

ventana.mainloop()

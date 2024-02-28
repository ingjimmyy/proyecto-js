from tkinter import*
from tkinter.ttk import*
from tkinter import messagebox


ventana=Tk()
ventana.title("mas funcionalidades en python tkinter")

ventana.geometry("350x200")

#COMBOBOX PYTHON TKINTER
"""
combo1=Combobox(ventana)
combo1['values']=("Jimmy","Sebastian","Sandra","Leidy","Wilson")
combo1.current(3)
combo1.grid(column=0,row=0)

label1=Label(ventana,text="",font=("arial bold",15))
label1.grid(column=0,row=1)

def saludarA():
    mensaje="Hola"+str(combo1.get())
    label1.config(text=mensaje)
boton1=Button(ventana,text="SALUDAR",command=saludarA)
boton1.grid(column=0,row=2)
"""
#COMBOBOX PYTHON TKINTER

#RADIOBUTTON PYTHON TKINTER

seleccionRBN=IntVar()
rbn1=Radiobutton(ventana,text="primero",value=1,variable=seleccionRBN)
rbn2=Radiobutton(ventana,text="segundo",value=2,variable=seleccionRBN)
rbn3=Radiobutton(ventana,text="tercero",value=3,variable=seleccionRBN)

rbn1.grid(column=0,row=0)
rbn2.grid(column=1,row=0)
rbn3.grid(column=2,row=0)

#label1=Label(ventana,text="",font=("arial bold",15))
#label1.grid(column=0,row=1)

def posicionRBN():
    mensaje="posicion"+str(seleccionRBN.get())
#    label1.config(text=mensaje)
    messagebox.showinfo("mensaje",mensaje)
    
boton1=Button(ventana,text="SALUDAR",command=posicionRBN)
boton1.grid(column=0,row=1)
#RADIOBUTTON PYTHON TKINTER
ventana.mainloop()
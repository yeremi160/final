from tkinter import *

#funcion
def binario():
    lblbinario=Label(root,text="hola"+ entrada1.get(),font=("Agency FB",14)).place(x=80,y=210)


root = Tk()

ancho = 460
alto = 250

root.geometry(str(ancho)+"x"+str(alto))
root.title("FINAL")

#titulo
saludo = Label(text="Bienvenido",font=("Agency FB",14)).place(x=190,y=5)
def dias():
    lbldias=Label(root,text="hola"+ entrada2.get(),font=("Agency FB",14)).place(x=80,y=210)
def par():
    lblpar=Label(root,text="hola"+ entrada3.get(),font=("Agency FB",14)).place(x=80,y=210)
def vocales():
    lblvocales=Label(root,text="hola"+ entrada4.get(),font=("Agency FB",14)).place(x=80,y=210)
def name():
    lblname=Label(root,text="hola"+ entrada5.get(),font=("Agency FB",14)).place(x=80,y=210)

#label
lblnombre=Label(text="Nombre",font=("Agency FB",14)).place(x=80,y=30)
entrada1=StringVar()
txtnombre=Entry(root,textvariable=entrada1,width=30).place(x=135,y=40)

lblapellido=Label(text="Apellido",font=("Agency FB",14)).place(x=80,y=60)
entrada2=StringVar()
txtape=Entry(root,textvariable=entrada2,width=30).place(x=135,y=70)

lbldia=Label(text="Dia",font=("Agency FB",14)).place(x=80,y=90)
entrada3=StringVar()
txtdia=Entry(root,textvariable=entrada3,width=30).place(x=135,y=100)

lblmes=Label(text="Mes",font=("Agency FB",14)).place(x=80,y=120)
entrada4=StringVar()
txtmes=Entry(root,textvariable=entrada4,width=30).place(x=135,y=130)

lblaño=Label(text="Año",font=("Agency FB",14)).place(x=80,y=150)
entrada5=StringVar()
txtaño=Entry(root,textvariable=entrada5,width=30).place(x=135,y=160)

#botones
btnFuncion1 = Button(root, text= "FUNCION 1",command=binario,font=("Agency FB",10),width=10).place(x=74,y=180)

btnFuncion1 = Button(root, text= "FUNCION 2",command=dias,font=("Agency FB",10),width=10).place(x=124,y=180)

btnFuncion1 = Button(root, text= "FUNCION 3",command=par,font=("Agency FB",10),width=10).place(x=174,y=180)

btnFuncion1 = Button(root, text= "FUNCION 4",command=vocales,font=("Agency FB",10),width=10).place(x=224,y=180)

btnFuncion1 = Button(root, text= "FUNCION 5",command=name,font=("Agency FB",10),width=10).place(x=274,y=180)






root.mainloop()
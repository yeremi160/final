from tkinter import *
root = Tk()

ancho = 460
alto = 250

root.geometry(str(ancho)+"x"+str(alto))
root.title("FINAL")
#titulo
saludo = Label(text="Bienvenido",font=("Agency FB",14)).place(x=190,y=5)
#label
lblnombre=Label(text="Nombre",font=("Agency FB",14)).place(x=80,y=30)
entrada1=StringVar()
txtnombre=Entry(root,textvariable=entrada1,width=30).place(x=135,y=40)












root.mainloop()
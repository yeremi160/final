from tkinter import *
from datetime import date
from datetime import datetime

raiz = Tk()
raiz.geometry("400x400")
raiz.title("Examen final")
code= Frame()
code.pack()
bienvenido = Label(code, text="BIENVENIDO")
bienvenido.grid(row=0, column=1)
bienvenido.config(font=('Arial black', 14))


name = StringVar()
ape = StringVar()
dia = IntVar()
mes = IntVar()
ano = IntVar()


def vida():
    fechaString = f"{ano.get()}-{mes.get()}-{dia.get()}"
    date_object = datetime.strptime(fechaString, '%Y-%m-%d')

    today= datetime.today()
    xx = today
    xy = date_object
    result1 = abs(xx-xy).days 

    final = f"Naciste en {date_object} has vivido:  {result1} dias"

    lblResp.configure(text = final)

    


#--Conteo de Letras de Nombre 
#--Conteo de Vocales y vocalesConsonantes
#--Nombre al alReves


#--Nombre
lblname= Label(code, text="Nombre:",font=("Arial black",10))
lblname.grid(row=1, column=0)
lblname.config(padx=10, pady=10)
txtNom=Entry(code, textvariable =code)
txtNom.grid(row=1, column=1)
#--Apellido
lblape=Label(code, text="Apellido:",font=("Arial black",10))
lblape.grid(row=2, column=0)
lblape.config(padx=10, pady=10)
txtApellido=Entry(code, textvariable =ape)
txtApellido.grid(row=2, column=1)
#--Día
lbldia=Label(code, text="Día: ",font=("Arial black",10))
lbldia.grid(row=3, column=0)
lbldia.config(padx=10, pady=10)
txtDia=Entry(code, textvariable =dia)
txtDia.grid(row=3, column=1)
#--Mes
lblmes=Label(code, text="Mes: ",font=("Arial black",10))
lblmes.grid(row=4, column=0)
lblmes.config(padx=10, pady=10)
txtMes=Entry(code, textvariable =mes)
txtMes.grid(row=4, column=1)
#--Año
lblano=Label(code, text="Año: ",font=("Arial black",10))
lblano.grid(row=5, column=0)
lblano.config(padx=10, pady=10)
txtanio=Entry(code, textvariable =ano)
txtanio.grid(row=5, column=1)
#--Botones
btnFuncion1 = Button(code, text="Función 1",font=("Agency FB",12))
btnFuncion1.grid(row=6, column=0)
btnFuncion1.config(padx=3, pady=3)
btnFuncion2 = Button(code, text = "Función 2", command=vida,font=("Agency FB",12))
btnFuncion2.grid(row=6, column=1)
btnFuncion2.config(padx=3, pady=3)
btnFuncion3 = Button(code, text = "Función 3",font=("Agency FB",12))
btnFuncion3.grid(row=6, column=2)
btnFuncion3.config(padx=3, pady=3)
btnFuncion4 = Button(code, text = "Función 4",font=("Agency FB",12))
btnFuncion4.grid(row=6, column=3)
btnFuncion4.config(padx=3, pady=3)
btnFuncion5 = Button(code, text = "Función 5",font=("Agency FB",12))
btnFuncion5.grid(row=6, column=4)
btnFuncion5.config(padx=3, pady=3)
#--Respuesta
lblResp=Label(code, text="")
lblResp.grid(row=15, column=6)
lblResp.config(padx=5, pady=5)
lblR=Label(code)
lblR.grid(row=18, column=6)
lblR.config(padx=5, pady=5)

raiz.mainloop()

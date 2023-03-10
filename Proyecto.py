from tkinter import*
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np
from sympy import symbols
from sympy import lambdify
from sympy import sympify
import sympy as sp

"""Funciones"""
def calcular():
    global etiqueta6
    if etiqueta6 is not None:
            etiqueta6.destroy()
    destruirInstancias(ttk.Treeview) 
    try:
        contador=1
        erroraproximado=1
        xanterior=0
        x=symbols('x')
        fn = sympify (Textbox1.get(1.0, "end-1c" ))
        f= lambdify(x,fn)
        a= float(Textbox2.get(1.0, "end-1c" ))
        b= float(Textbox3.get(1.0, "end-1c" ))
        criterioerror= float(Textbox4.get(1.0, "end-1c" ))
        if f(a)*f(b)<0:
            tabla= ttk.Treeview(ventana, columns=("Xa","Xb","xr","ea"))         
            tabla.column("#0", width=80,anchor=CENTER)
            tabla.column("Xa", width=150,anchor=CENTER)
            tabla.column("Xb", width=150,anchor=CENTER)
            tabla.column("xr", width=150,anchor=CENTER)
            tabla.column("ea", width=150,anchor=CENTER)
            tabla.heading("#0",text="Iteración",anchor=CENTER)
            tabla.heading("Xa",text="Xa",anchor=CENTER)
            tabla.heading("Xb",text="Xb",anchor=CENTER)
            tabla.heading("xr",text="xr",anchor=CENTER)
            tabla.heading("ea",text="ea",anchor=CENTER)
            tabla.place(x=60, y=330)
            while erroraproximado>criterioerror:
                if(combo.get()=="Bisección"):
                    xr=(a+b)/2
                else:
                    xr= b-((f(b)*(b - a))/(f(b) - f(a)))
                erroraproximado= abs((xr-xanterior)/xr)
                tabla.insert("",END,text=contador,values=(a,b,xr,round(erroraproximado*100,9)))
                if f(xr)*f(a)<0:
                    b=xr
                else:
                    a=xr
                xanterior=xr
                contador+=1
            etiqueta6=Label(text="El valor de x es: "+ str(round(xr,9))+" Con un error de "+str(round(erroraproximado*100,9))+"%", fg="black",font=("Times new Roman", 12))
            etiqueta6.place(x=120,y=580)
        else:
                etiqueta6=Label(text="La función no tiene una raíz en el intervalo de xa: "+str(a)+" y de xb "+str(b), fg="black",font=("Times new Roman", 12))
                etiqueta6.place(x=150,y=320)
    except Exception as e:
        destruirInstancias(ttk.Treeview)
        if isinstance(e, ZeroDivisionError):
            etiqueta6=Label(text="No se pudo calcular la raiz con el error esperado porque durante el proceso se produjo una excepción de división con 0", fg="black",font=("Times new Roman", 12))
        else:
            etiqueta6=Label(text="Ingrese correctamente los datos", fg="black",font=("Times new Roman", 12))
        etiqueta6.place(x=150,y=320)
    

def graficar():
    global canvas
    destruirInstancias(NavigationToolbar2Tk)
    try:
        if canvas is not None:
            canvas.get_tk_widget().destroy()
        x = symbols('x')
        fn = sympify(Textbox1.get(1.0, "end-1c"))
        f = lambdify(x, fn)
        xpts = np.linspace(-10, 10)
        fig, ax = plt.subplots(figsize=(5, 3))
        ax.plot(xpts, f(xpts))
        ax.set_title("Gráfica de la función")
        ax.axhline(color="black")
        ax.axvline(color="black")
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.grid(True, which='both')
        ax.set_ylim([-15, 15])   
        canvas = FigureCanvasTkAgg(fig, master=ventana)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        toolbar = NavigationToolbar2Tk(canvas,ventana)
        toolbar.update()
        toolbar.pack(side=tk.BOTTOM, fill=tk.X)
        canvas.get_tk_widget().place(x=405, y=10)
    except(Exception):
        etiqueta6=Label(text="Ingrese correctamente la función", fg="black",font=("Times new Roman", 12))
        etiqueta6.place(x=500,y=100)

def destruirInstancias(objeto):
    for widget in ventana.winfo_children():
        if isinstance(widget, objeto):
            widget.destroy()
        

"""variables globales"""
ventana = Tk()
etiqueta6=Label(text="", fg="black",font=("Times new Roman", 12))
canvas = FigureCanvasTkAgg()
"""Creación de la ventana y sus componentes gráficos"""
ventana.title("Métodos Cerrados")
ventana.resizable(False, False)
ventana.geometry("920x682")
ventana.iconbitmap("Files/raiz-cuadrada.ico")
etiqueta1=Label(text="Función", fg="black",font=("Times new Roman", 12))
etiqueta1.place(x=60,y=35)
etiqueta2=Label(text="Método", fg="black",font=("Times new Roman", 12))
etiqueta2.place(x=60,y=80)
etiqueta3=Label(text="xa", fg="black",font=("Times new Roman", 12))
etiqueta3.place(x=60,y=115)
etiqueta4=Label(text="xb", fg="black",font=("Times new Roman", 12))
etiqueta4.place(x=60,y=160)
etiqueta5=Label(text="Error", fg="black",font=("Times new Roman", 12))
etiqueta5.place(x=60,y=200)
Textbox1= Text(ventana,width=20, height=0.5)
Textbox1.place(x=150,y=35)
Textbox2= Text(ventana,width=5, height=0.5)
Textbox2.place(x=150,y=115)
Textbox3= Text(ventana,width=5, height=0.5)
Textbox3.place(x=150,y=160)
Textbox4= Text(ventana,width=30, height=0.5)
Textbox4.place(x=150,y=200)
combo= ttk.Combobox(ventana)
combo.place(x=150, y=80)
combo["values"]=("Bisección", "Falsa Posición")
combo.current(0)
btGraficar= Button(ventana, text="Graficar", fg="black", font=("Times new Roman", 12), command=graficar)
btGraficar.pack()
btGraficar.place(x=325,y=30)
btCalcular= Button(ventana, text="Calcular", fg="black", font=("Times new Roman", 12), command=calcular)
btCalcular.place(x=150,y=230)
ventana.mainloop()
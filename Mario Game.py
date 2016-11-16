
import tkinter
from tkinter import ttk

#Creacion Menu
MP= tkinter.Tk()
MP.geometry("771x600")
MP.title("Menu Mario")

#Imagen Del Menu
canvasIma= tkinter.Canvas(MP,width=771,height=600)
imagenL= tkinter.PhotoImage(file="Mapa Mario.png")
canvasIma.create_image(385.5,300,image=imagenL)
canvasIma.focus_set()
canvasIma.pack()

#Minimizacion
MP.withdraw()
def Menu():
    global MP
    X= tkinter.Toplevel(MP)
    canvasIma2= tkinter.Canvas(X,width=771,height=600)
    menuP= tkinter.PhotoImage(file="MenuFinal.png")
    canvasIma2.create_image(385.5,300,image=menuP)
    canvasIma2.pack()
    def Boton2Players():
        MP.iconify()
        X.withdraw()
    Boton2pla=tkinter.Button(X,text="2 Player",font=("Arial",18),command=Boton2Players)
    Boton2pla.place(x=305,y=100)
    X.resizable()
    X.mainloop()
Menu()
MP.resizable()    
MP.mainloop()




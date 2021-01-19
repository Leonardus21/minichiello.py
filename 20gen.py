from tkinter import *
from tkinter import filedialog 

def browseFiles(): 
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", ".txt"), ("all files", ".")))

    label_file_explorer.configure(text="File aperto: "+filename) 

def crea_grafico():
    import string
    import numpy as np
    import matplotlib.pyplot as plt

    f = open(filename, 'r')


    coordX = []
    coordY = []
    for riga in f:
        valori = str(riga)
        Nval = len(valori)
        valori = valori.strip('\n') 
        valori = valori.split(',')
        valori = list(valori)
        print(valori)
        coordX.append(int(valori[0])) 
        coordY.append(int(valori[1])) 

    f.close()

    print ("X: ",coordX)
    print ("Y: ",coordY)

    coordX.sort()
    coordY.sort()

    print("liste ordinate:") 
    print ("X: ",coordX)
    print ("Y: ",coordY)

    print(type(coordX))
    print(type(coordY))


    plt.scatter(coordX,coordY)
    plt.ylabel('some numbers')
    plt.show()

window = Tk() 

window.title('Interfaccia Grafica')

window.geometry("800x600") 

window.config(background = "green") 

label_file_explorer = Label(window, text = "Inserisci un file di testo e genera un grafico", width = 116, height = 3, fg = "black")

button_explore = Button(window, text = "Inserisci file di testo", command = browseFiles)

button_exit = Button(window, text = "Esci", command = exit)

button_genera_grafico = Button(window, text = "Crea grafico", command = crea_grafico) 

label_file_explorer.grid(column = 1, row = 1) 

button_explore.grid(column = 1, row = 2) 

button_exit.grid(column = 1,row = 4) 

button_genera_grafico.grid(column = 1, row = 3)

window.mainloop()

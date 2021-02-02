import numpy as np
import matplotlib.pyplot as plt
from guizero import App, Text, PushButton, TextBox, Picture


def mostra_grafico():
    f = a.value
    f = open(f, 'r')
    coordX = []
    coordY = []

    for riga in f:
        valori = str(f.readline())  
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


    print(type(coordX))
    print(type(coordY))

    plt.title("Grafico a dispersione")
    plt.scatter(coordX,coordY)
    plt.savefig("grafico.png", dpi = 100, facecolor = "ivory")
    immagine = Picture(app, image = "grafico.png")

app = App(title = "Interfaccia grafica", bg = "wheat", width = 700, height = 610) 
introduzione = Text(app, text = "Inserisci il nome di un file di testo e genera un grafico")


a = TextBox(app, text = "Nome file")
pulsante = PushButton(app, text = "Genera grafico", command = mostra_grafico)
app.display()

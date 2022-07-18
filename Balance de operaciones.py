import schedule
import time
import random

#Clase de los TXNs pendientes
class TXNsPendientes:
    def __init__(self, numero, monto, nsegs):
        self.numero = numero
        self.monto = monto
        self.nsegs = nsegs

#Función para sumar el balance en el archivo de Balance.txt
def sumar_balance():
    #Abrir el archivo y seleccionar una linea random
    TXNs = open('TXNs.txt').read().splitlines() 
    indexl = random.choice(range(len(TXNs)))
    myline = TXNs[indexl]
    del TXNs[indexl] #Borra la linea escogida de la lista de lineas
    #Reescribe el archivo sin la línea escogida
    TXNsn = open('TXNs.txt','w')
    for line in TXNs:
        TXNsn.write(line + "\n")
    TXNsn.close()
    monto = myline.split("$") #Separa la linea para poder tomar el valor del monto
    #Abrir el archivo para hacer la suma del monto escogido con el balance
    balance = open("Balance.txt", "r") 
    bal = balance.readlines()
    bal[0] = str(round(float(bal[0])+float(monto[1]),2))
    balance = open ("Balance.txt","w")
    balance.writelines(bal)
    balance.close()
    print("Balance actualizado")
    return myline

TXNsPen = [] #Lista para almacenar las lineas escogidas aleatorias

#Función para tomar una línea de los TXNs obtenidos y añadirla al archivo de ApprovedTXNs.txt
def ATXNs(linea): #Pasamos la linea de la función de sumar balance
    atrib = linea.split(" ") #La guardamos dividida por un espacio
    s = random.randint(15,280) #Variable de segundos
    Txnsp = TXNsPendientes(atrib[0],atrib[2],s) #Guardamos los valores de la linea con la clase TXNsPendientes
    TXNsPen.append(Txnsp) #Añadimos el objeto a una lista
    i = 0
    #Mientras que la lista no esté vacía, procedemos
    if len(TXNsPen) != 0:
        #Ciclo para añadir el elemento al archivo de ApprovedTXNs.txt con respecto a los segundos   
        while s != 0:
            time.sleep(1)
            s = s-1
            if s == 0:
                newl = TXNsPen[i]
                ApprovedTXNs = open ("ApprovedTXNs.txt","a")
                ApprovedTXNs.write(str(newl.numero)+' ¿? '+str(newl.monto)+'\n')
                ApprovedTXNs.close()
                print("ApprovedTXNs actualizado")
                del TXNsPen[i]
            i += 1
            if i == len(TXNsPen):
                i= 0
    else:
        print("No hay TXNs pendientes")

while True:
    lin=sumar_balance()
    n = random.randint(30,300) 
    time.sleep(n)
    ATXNs(lin)


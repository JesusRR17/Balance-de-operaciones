from datetime import datetime
import time
import re

#Función para sacar el balance del archivo
def balance():
    bal = open("Balance.txt").read().splitlines()
    balance = bal[0]
    print(balance + "\n")
    return balance
mensaje = "hola mundo"
#Función para escribir en el archivo de signals.txt
def WriteSignal(mensaje):
    signals = open("Signals.txt","a")
    signals.write(mensaje + '\n')
    signals.close()
#Función que revisa si ApprovedTXNs.txt fue modificado y otras cosas
def ApprovedTXNs(cnol, monto_dca):
    atx = open("ApprovedTXNs.txt").read().splitlines() 
    nol = len(atx)
    if nol == cnol:
        # No hace nada porque no hubo cambios    
        pass
    else:
        tiempo_actual = datetime.now()
        tiempo_actual = tiempo_actual.strftime("%H:%M:%S %d/%b/%Y")
        ultima_linea = atx[-1]
        ultima_linea_splits = re.split(' |\n',ultima_linea)
        mensaje = ("Sent " + ultima_linea_splits[2] + " to " + ultima_linea_splits[0])
        print(mensaje+ "\n")
        mensaje = (mensaje + " at " + tiempo_actual)
        monto = ultima_linea_splits[2].split("$")
        monto = monto[1].replace(".","")
        monto_t = int(monto)
        monto_dca = monto_dca + monto_t
        WriteSignal(mensaje)
    return(monto_dca)

# Función que revisa cuantas lineas tiene approvedtxns.txt
def act_ATXNs():
    atx = open("ApprovedTXNs.txt").read().splitlines()
    nol = len(atx)
    return nol

monto_db = 0
monto_dca = 0
monto_dsa = 0

while(True):
    tiempo_actual = datetime.now()
    tiempo_actual = tiempo_actual.strftime("%H:%M:%S %d/%b/%Y")
    cnol = act_ATXNs() #Revisamos la cantidad de lineas que tiene el archivo ApprovedTXNs.txt
    time.sleep(0.5) # cada 500 milisegundos se ejecuta
    monto_dca = ApprovedTXNs(cnol, monto_dca) #Ejecutamos la función que revisa si ApprovedTXNs.txt fue modificado y actualizamos el monto dca
    monto_dsa = monto_db - monto_dca
    #Imprimimos el monto del delta aprobado y delta no aprobado en la consola y en el archivo Signals.txt
    mensaje = ("[Delta aprobado]: " + str(monto_dca) + " - " + " [Delta no aprobado]: " + str(monto_dsa) + " at " + tiempo_actual)
    print(mensaje + "\n")
    WriteSignal(mensaje)
    #Regresamos el monto de delta con aprobación y delta del balance a 0
    monto_dca = 0
    monto_db = 0
    #Imprimimos una fila de guiones en la consola y en el archivo Signals.txt
    guiones = "-------------------------------------------------------------------------"
    print(guiones+ "\n")
    WriteSignal(guiones)
    mensaje= ()
    guiones = ()

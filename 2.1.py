import matplotlib.pyplot as plt
from os import system
from random import randint

def generador_GCL():
        numeros = []
        m = 2**48 #modulo
        a = 25214903917  #multipliador
        c = 11 #Incremento
        semilla = 14758
        numeros.append(semilla)

        for i in range(1,100):
            nro = (a*numeros[i-1] + c) % m
            numeros.append(nro)
        print("GCL:     ",numeros)

def generador_pmc():
    seed = 6923
    n=100 #cantidad de numeros generados
    numeros = [seed]
    sem = []
    sem2 =[]
    for i in range(1,n):
        x = numeros[i - 1] ** 2
        if(len(str(x))<8):
            x=completa_ceros(x)
        sem = [int(a) for a in str(x)]
        sem2 = sem[2:6]
        seed =int(''.join(map(str, sem2)))
        numeros.append(seed)
    print("PMC:     ",numeros)

def completa_ceros(sem):
    sem = str(sem)
    for i in range(0, (8 - len(sem))):
        sem = '0' + sem
    return sem



numeros=[]

generador_pmc()
generador_GCL()

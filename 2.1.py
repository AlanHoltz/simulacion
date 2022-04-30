import matplotlib.pyplot as plt
from os import system
from random import randint
from sklearn import preprocessing
import numpy as np

def generador_GCL():
        global numeros
        numeros_poker  = []
        m = 2**48 #modulo
        a = 25214903917  #multipliador
        c = 11 #Incremento
        semilla = 14758
        numeros.append(semilla)

        for i in range(1,100):
            nro = (a*numeros[i-1] + c) % m
            nro_p = [int(a) for a in str(nro)]
            nro_p1 = nro_p[1:6]
            numeros.append(nro)
            numeros_poker.append(nro_p1)
        prueba_poker(numeros_poker)
        #print("GCL:     ",numeros)

def generador_pmc():
    global numeros
    numeros_poker =[]
    seed = 6923
    n=10000 #cantidad de numeros generados
    numeros = [seed]
    sem = []
    sem2 =[]
    for i in range(1,n):
        x = numeros[i - 1] ** 2
        if(len(str(x))<8):
            x=completa_ceros(x)
        sem = [int(a) for a in str(x)]
        sem2 = sem[2:6]
        sem3 = sem[1:6]
        seed =int(''.join(map(str, sem2)))
        numeros_poker.append(sem3)
        numeros.append(seed)
    prueba_poker(numeros_poker)
    #print(numeros_poker)
    #print("PMC:     ",numeros)

def completa_ceros(sem):
    sem = str(sem)
    for i in range(0, (8 - len(sem))):
        sem = '0' + sem
    return sem

def normalizar ():
    global numeros_normalizado
    list = np.array(numeros).reshape(-1, 1)
    scaler = preprocessing.MinMaxScaler()
    numeros_normalizado = scaler.fit_transform(list)
    print('Numeros normalizados', numeros_normalizado)


def prueba_poker(numeros):
    c = 0
    x = 0
    p2, p1, f, po, q, pa, t = 0, 0, 0, 0, 0, 0, 0
    esperada = []
    probabilidad = []
    observada = []
    fila = []
    columna = []
    que_hay = []
    lista_nueva = numeros
    n = len(lista_nueva)
    print(lista_nueva)
    for i in range(0,n):
        que_hay.append('')

    probabilidad.append(0.30240)
    probabilidad.append(0.00010)
    probabilidad.append(0.009)
    probabilidad.append(0.00450)
    probabilidad.append(0.07200)
    probabilidad.append(0.10800)
    probabilidad.append(0.50400)

    for i in range(len(probabilidad)): #probabilidad de cada jugada
        e = n * probabilidad[i]
        esperada.append(e)

    for i in range(len(lista_nueva)): #genera una lista donde guarda la cantidad de veces q se repitio el digito en el nro, ej: nro = 44266 array = [2,2,1,2,2]
        for a in range(0, 5):
            compara = lista_nueva[i][a]
            for j in range(0, 5):
                if compara == lista_nueva[i][j]:
                    c = c + 1
            columna.append(c)
            c = 0
        fila.append(columna)
        columna = []
    #print(fila)
    for h in range(len(fila)): # genera observadas=[] donde guarda la cantidad observada por jugada
        cuenta = 0
        poker = 0
        quintilla = 0
        tercia = 0

        for z in range(0, 5):
            if 2 == fila[h][z]:
                cuenta += 1
            if 4 == fila[h][z]:
                poker += 1
            if 5 == fila[h][z]:
                quintilla += 1
            if 3 == fila[h][z]:
                tercia += 1
        if cuenta == 4 and len(set(lista_nueva[h])) == 3:
            que_hay[h] = 'par2'
            p2 += 1

        elif cuenta == 2 and len(set(lista_nueva[h])) == 4:
            que_hay[h] = 'par1'
            p1 += 1

        elif cuenta == 2 and tercia == 3 and len(set(lista_nueva[h])) == 2:
            que_hay[h] = 'full'
            f += 1

        elif poker == 4 and len(set(lista_nueva[h])) == 2:
            que_hay[h] = 'poker'
            po += 1

        elif quintilla == 5 and len(set(lista_nueva[h])) == 1:
            que_hay[h] = 'quintilla'
            q += 1

        elif len(set(lista_nueva[h])) == 5:
            que_hay[h] = 'pachuca'
            pa += 1

        elif tercia == 3 and len(set(lista_nueva[h])) == 3:
            que_hay[h] = 'tercia'
            t += 1

    observada.append(pa)
    observada.append(q)
    observada.append(f)
    observada.append(po)
    observada.append(t)
    observada.append(p2)
    observada.append(p1)
    #print("Pachuca:",observada[0],
    #      "Quintilla:",observada[1],
    #      "Full:",observada[2],
    #      "Poker:",observada[3],
    #      "Tercia:",observada[4],
    #      "Par doble:",observada[5],
    #      "Par solo:",observada[6])
    for i in range(0,7):
        x = ((esperada[i]-observada[i])**2)/esperada[i]
    chi_cuadrado = 12.5916
    if x <= chi_cuadrado:
        print("los números generados son estadísticamente independientes.")
    else:
        print("Se rechaza que los numeros son independientes. No son aleatorios")



numeros=[]
numeros_normalizado = []
generador_pmc()
#generador_GCL()
#normalizar()

import matplotlib.pyplot as plt
from os import system
from random import randint
import math
import statistics

def prueba_poker():
    c = 0
    x = 0
    p2, p1, f, po, q, pa, t = 0, 0, 0, 0, 0, 0, 0
    esperada = []
    probabilidad = []
    observada = []
    fila = []
    columna = []
    que_hay = []

    lista_nueva = [[4, 0, 6, 5, 1], [4, 0, 6, 5, 1], [4, 0, 6, 5, 1], [4, 0, 6, 5, 1], [7, 7, 9, 5, 8], [7, 7, 2, 2, 9],
                   [0, 0, 9, 9, 9], [2, 2, 2, 2, 6], [0, 0, 0, 0, 0],
                   [6, 6, 6, 2, 1], [6, 6, 6, 2, 1], [6, 6, 6, 2, 1]]
    n = len(lista_nueva)
    for i in range(0, len(lista_nueva)):
        que_hay.append('')

    probabilidad.append(0.30240)
    probabilidad.append(0.00010)
    probabilidad.append(0.009)
    probabilidad.append(0.00450)
    probabilidad.append(0.07200)
    probabilidad.append(0.10800)
    probabilidad.append(0.50400)

    for i in range(len(probabilidad)):
        e = n * probabilidad[i]
        esperada.append(e)

    for i in range(len(lista_nueva)):
        for a in range(0, 5):
            compara = lista_nueva[i][a]
            for j in range(0, 5):
                if compara == lista_nueva[i][j]:
                    c = c + 1
            columna.append(c)
            c = 0
        fila.append(columna)
        columna = []

    for h in range(len(fila)):
        cuenta = 0
        individuales = 0
        poker = 0
        quintilla = 0
        tercia = 0

        for z in range(0, 5):
            if 2 == fila[h][z]:
                cuenta += 1
            if 1 == fila[h][z]:
                individuales += 1
            if 4 == fila[h][z]:
                poker += 1
            if 5 == fila[h][z]:
                quintilla += 1
            if 3 == fila[h][z]:
                tercia += 1
        if cuenta == 4 and individuales == 1 and len(set(lista_nueva[h])) == 3:
            que_hay[h] = 'par2'
            p2 += 1

        elif cuenta == 2 and individuales == 3 and len(set(lista_nueva[h])) == 4:
            que_hay[h] = 'par1'
            p1 += 1

        elif cuenta == 2 and tercia == 3 and len(set(lista_nueva[h])) == 2:
            que_hay[h] = 'full'
            f += 1

        elif poker == 4 and individuales == 1 and len(set(lista_nueva[h])) == 2:
            que_hay[h] = 'poker'
            po += 1

        elif quintilla == 5 and len(set(lista_nueva[h])) == 1:
            que_hay[h] = 'quintilla'
            q += 1

        elif individuales == 5 and len(set(lista_nueva[h])) == 5:
            que_hay[h] = 'pachuca'
            pa += 1

        elif individuales == 2 and tercia == 3 and len(set(lista_nueva[h])) == 3:
            que_hay[h] = 'tercia'
            t += 1

    observada.append(pa)
    observada.append(q)
    observada.append(f)
    observada.append(po)
    observada.append(t)
    observada.append(p2)
    observada.append(p1)
    print(observada)
    for i in range(0, 7):
        x = ((esperada[i] * observada[i]) ** 2) / esperada[i]
    print(x)
    chi_cuadrado = 12.5916
    if x <= chi_cuadrado:
        print("No se puede rechazar que los numeros son independientes")


prueba_poker()
import matplotlib.pyplot as plt
from os import system
from random import randint
import random
from sklearn import preprocessing
import numpy as np
import pandas as pd
import seaborn as sns
import statistics
import math
from scipy import stats
from scipy.stats import norm


def generador_python():
    global numeros_poker
    columna = []
    for i in range(cantidad_numeros):
        numeros_normalizados.append(random.random())
        numeros.append(random.randint(0, 100000))

    for i in range(0, cantidad_numeros): # genera una nueva lista con los numeros normalizados numeros_poker=[] para pasarlo a prubea_poker
        cadena = str(numeros_normalizados[i])
        separador = '.'
        decimal = cadena.split(separador)
        x = decimal[1]
        for i in range(0,len(x)-1):
            x0 = x[i]
            columna.append(x0)
        poker = columna[1:6]
        numeros_poker.append(poker)
        columna = []
    print("------------------------------------------------------------")
    print("Generador PYTHON:")
    prueba_poker(numeros_poker)
    prueba_de_rachas()
    prueba_SK()
   # prueba_bondad_ajuste()

def generador_GCL(cantidad_numeros):
        global numeros
        m = 2**48 #modulo
        a = 25214903917  #multipliador
        c = 11 #Incremento
        semilla = 14758
        numeros.append(semilla)
        for i in range(1, cantidad_numeros):
            nro = (a*numeros[i-1] + c) % m
            numeros.append(nro)
        print("------------------------------------------------------------")
        print("Generador Congruencial Lineal:")
        normalizar()

def generador_pmc(cantidad_numeros):
    global numeros
    seed = 6923
    numeros = [seed]
    for i in range(1,cantidad_numeros):
        x = numeros[i - 1] ** 2
        if(len(str(x))<8):
            x = completa_ceros(x)
        sem = [int(a) for a in str(x)]
        sem2 = sem[2:6]
        seed =int(''.join(map(str, sem2)))
        numeros.append(seed)
    print("------------------------------------------------------------")
    print("Generador Parte Media del Cuadrado:")
    normalizar()

    #print("PMC:     ",numeros)

def completa_ceros(sem):
    sem = str(sem)
    for i in range(0, (8 - len(sem))):
        sem = '0' + sem
    return sem

def normalizar ():
    global numeros_normalizados
    global numeros_poker
    columna=[]
    list = np.array(numeros).reshape(-1, 1)
    scaler = preprocessing.MinMaxScaler()
    numeros_normalizados = scaler.fit_transform(list)

    for i in range(0, cantidad_numeros): # genera una nueva lista con los numeros normalizados numeros_poker=[] para pasarlo a prubea_poker
        cadena = str(numeros_normalizados[i])
        separador = '.'
        decimal = cadena.split(separador)
        x = decimal[1]
        for i in range(0,len(x)-1):
            x0 = x[i]
            columna.append(x0)
        poker = columna[1:6]
        numeros_poker.append(poker)
        columna = []

    prueba_poker(numeros_poker)
    prueba_de_rachas()
    prueba_SK()
    #prueba_bondad_ajuste()

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
    lista_nueva = []
    for i in range(0, len(numeros)):
        num = list(map(int, numeros[i]))
        lista_nueva.append(num)
    n = len(lista_nueva)
    #print("lista nueva:",lista_nueva)
    for i in range(0, n):
        que_hay.append('')
    probabilidad.append(0.30240) #pachuca
    probabilidad.append(0.00010) #quintilla
    probabilidad.append(0.009) #full
    probabilidad.append(0.00450) #poker
    probabilidad.append(0.07200) #tercia
    probabilidad.append(0.10800) #par2
    probabilidad.append(0.50400) #par

    for i in range(len(probabilidad)): #probabilidad esperada de cada jugada
        e = n * probabilidad[i]
        esperada.append(e)

    for i in range(len(lista_nueva)): #genera una lista donde guarda la cantidad de veces q se repitio el digito en el nro, ej: nro = 44266 array = [2,2,1,2,2]
        if lista_nueva[i] == []:
            lista_nueva[i]= [0, 0, 0, 0, 0]
        while len(lista_nueva[i])<5 :
            lista_nueva[i].append(0)
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

    observada.append(pa) #pachuca
    observada.append(q) #quintilla
    observada.append(f) #full
    observada.append(po) #poker
    observada.append(t) #tercia
    observada.append(p2) #par2
    observada.append(p1) #par

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
        print("PRUEBA DE POKER: Los números generados son estadísticamente independientes.")
    else:
        print("PRUEBA DE POKER: Se rechaza que los numeros son independientes.")

def prueba_de_rachas():
    rachas, n1, n2 = 0, 0, 0
    media = statistics.median(numeros)

    for i in range(len(numeros)):

        if (numeros[i] >= media and numeros[i - 1] < media) or \
                (numeros[i] < media and numeros[i - 1] >= media):
            rachas += 1

        if (numeros[i]) >= media:
            n1 += 1
        else:
            n2 += 1
    rachas_esp = ((2 * n1 * n2) / (n1 + n2)) + 1  # Número de corridas esperadas
    desv = math.sqrt((2 * n1 * n2 * (2 * n1 * n2 - n1 - n2)) / (
                ((n1 + n2) ** 2) * (n1 + n2 - 1)))  # Desviación estándar del número de carreras

    Z = (rachas - rachas_esp) / desv

    if (Z > -1.96 and Z < 1.96):  # Para un nivel de confianza del 95%
        print("PRUEBA DE RACHAS: Los numeros son aleatorios. ")
    else:
        print("PRUEBA DE RACHAS: No hay evidencia estadistica para apoyar la aleatoridad de los numeros. Los numeros no son aleatorios. ")

    #GRAFICA DE DISTRIBUCION NORMAL
    fig, ax = plt.subplots()
    x = np.arange(-5,5,0.01)
    y = stats.norm.pdf(x)
    plt.axvline(x=Z, ymin=0.0, ymax=0.90, label="Estadistico de prueba", color = 'r')
    plt.title('Distribución Normal (0,1)')  # Título del gráfico
    plt.ylabel('f(x)')  # Título del eje y
    plt.xlabel('X')  # Título del eje x
    plt.fill_between(x, y, 0, where=(x >= -1.96) & (x <= 1.96), color='g', label="Zona de NO rechazo")
    ax.legend()
    plt.plot(x,y)
    plt.show()


def prueba_SK ():
    frecuencia = []
    D =[]
    ordenados = sorted(numeros_normalizados) #ordena de forma ascendente
    for i in range (1, cantidad_numeros+1):
        frecuencia.append(i/cantidad_numeros)
    for i in range (0, cantidad_numeros):
        D.append(abs(ordenados[i]-frecuencia[i]))
    #for i in range(0, cantidad_numeros):
    #    print(D[i])
    maxi = max(D) # obtiene el mayor de D
    num_tabla = 1.36/math.sqrt(cantidad_numeros) # con un nivel de significancia del 0.05
    if maxi < num_tabla:
        print("PRUEBA DE SMIRNOV -KOLMOGOROV:Los numeros tienen una distribucion uniforme.")
    else:
        print("PRUEBA DE SMIRNOV -KOLMOGOROV: Los numeros NO tienen una distribucion uniforme.")

def prueba_bondad_ajuste():
    chi2 = 0
    intervalos = int(cantidad_numeros/math.sqrt(cantidad_numeros))
    #print("intervalos:",intervalos)
    obs = pd.cut(numeros, intervalos).value_counts()  #corta la lista en intervalos y cuenta las observaciones de cada intervalo
    #print("obs",obs)
    esperado = cantidad_numeros/intervalos
    for i in range(0,intervalos-1):
        x = ((obs[i]-esperado)**2)/esperado
        chi2 += x
    #print("chi calculado", chi2)
    chi2_tabla = 140.1697 #para grados de libertad = 99
    #se debe ir modificando en base a la tabla. Para grados de libertad: intervalos-1 y el nivel de confiaza va a ser siempre 0.05
    if chi2 < chi2_tabla:
         print("PRUEBA DE BONDAD DE AJUSTE CHI2: Los numeros tienen una distribucion uniforme.")
    else:
         print("PRUEBA DE BONDAD DE AJUSTE CHI2: Los numeros NO tienen una distribucion uniforme.")
    grafico_barras(obs,esperado,intervalos)

def grafica_dispersion():
    x = []
    y = []
    for i in range(0,cantidad_numeros):
        x.append(i)
    for i in range(0,cantidad_numeros):
        y.append(numeros_normalizados[i])
    plt.scatter(x,y, label='scatter')  # Dibuja diagrama de dispersión
    plt.legend()
    plt.show()

def grafico_barras(o,e,intervalos):
    print("INTERVALOS CANT",intervalos)
    obs=[]
    esp=[]
    interv =[]
    for i in range(0,intervalos-1):
        obs.append(o[i])
        esp.append(e)
        interv.append(i)
    # posicion de cada barra en el eje de X
    x = np.arange(len(interv))
    width = 0.40
    fig, ax = plt.subplots()
    # Genera las barras para el conjunto observado y esperado
    rects1 = ax.bar(x - width / 2, obs, width, label='observado')
    rects2 = ax.bar(x + width / 2, esp, width, label='esperado')
    ax.set_title('Observaciones y valor esperado para cada intervalo')
    ax.legend()
    plt.show()

cantidad_numeros = 1000  #tamaño de la lista de numeros generados

numeros=[]
numeros_normalizados = []
numeros_poker = []
generador_GCL(cantidad_numeros)
grafica_dispersion()


numeros=[]
numeros_normalizados = []
numeros_poker = []
generador_python()
grafica_dispersion()


numeros=[]
numeros_normalizados = []
numeros_poker = []
generador_pmc(cantidad_numeros)
grafica_dispersion()



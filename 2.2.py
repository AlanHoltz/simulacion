from random import random
from math import log,exp
import matplotlib.pyplot as plt
import pandas as pd

total_nros = 1500 #Cantidad de numeros a generar

#DISTRIBUCIONES
def distribucion_uniforme(a,b):
    return a + (b-a) * random()

def distribucion_exponencial(ex):
    return -ex*log(random())

def distribucion_gamma(k,a):
    tr = 1
    
    for i in range(0,k):
        tr *= random()

    return -log(tr)/a

def distribucion_normal(ex,stdx):
    sum = 0

    for i in range(0,12):
        sum += random()

    return stdx * (sum - 6) + ex


def distribucion_pascal(k,q):
    tr = 1
    qr = log(q)

    for i in range(0,k):
        tr *= random()

    return log(tr)/qr

def distribucion_binomial(n,p):
    x = 0

    for i in range(0,n):

        r = random()

        if r <= p:
            x += 1

    return x

def distribucion_hipergeometrica(tn,ns,p):
    x = 0
    pC = p
    tnC = tn

    for i in range(0,ns):
        s = 0
        r = random()

        if r <= pC:
            s = 1
            x += 1

    pC = (tnC * pC - s)/(tnC - 1)
    tnC -= 1


    return x

def distribucion_poisson(p):
    x = 0
    tr = 1
    b = exp(-p)

    while tr > b:
        x += 1
        tr *= random()

    return x

def distribucion_empirica_discreta():
    x = 0
    p = [0.273, 0.039, 0.192, 0.007, 0.124, 0.058, 0.062, 0.151, 0.047, 0.044]
    u = random()
    acum = 0
    
    while (u > acum) and (u > p[0]) :
        acum += p[x]
        x = x + 1
    if x == 0:
        return(x)
    else:
        return(x-1)




#GRAFICAS
def grafica_dispersion():
    plt.figure('DISPERSIÓN')
    plt.title('Dispersión de los valores generados')
    plt.xlabel('')
    plt.ylabel('Valor')
    plt.plot(generador(total_nros), 'o', label='Dispersión de la primera corrida', color='orange')
    plt.show()

def grafica_histograma():
    plt.figure('HISTOGRAMA')
    plt.title('Histograma de frecuencias de los valores generados')
    plt.xlabel('Valor generado')
    plt.ylabel('Frecuencia absoluta')
    plt.hist(generador(total_nros), color='green')
    plt.show()




def generador(n):
    numeros_generados = []
    for i in range(n):
                                        #PARA TESTEAR TODAS LAS DISTRIBUCIONES CAMBIAR ESTA LÍNEA CON UNA DE LAS FUNCIONES 
        numeros_generados.append(distribucion_binomial(400,0.8)) # <-------------------------------------------------------------------------------
                                        #QUE SE ENCUENTRAN ARRIBA RESPETANDO TODOS LOS PARÁMETROS
    return(numeros_generados);  


grafica_dispersion()
grafica_histograma()





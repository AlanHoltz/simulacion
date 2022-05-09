from random import random
from math import log,exp

# random() devuelve un número entre 0 y 1

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

##  FALTA IMPLEMENTAR LA DISTRIBUCIÓN EMPÍRICA DISCRETA




def generador(n):
    for i in range(0,n):
                                        #PARA TESTEAR TODAS LAS DISTRIBUCIONES CAMBIAR ESTA LÍNEA CON UNA DE LAS FUNCIONES 
        nG = distribucion_poisson(0.35) # <-------------------------------------------------------------------------------
                                        #QUE SE ENCUENTRAN ARRIBA RESPETANDO TODOS LOS PARÁMETROS
        print(nG);

generador(300)





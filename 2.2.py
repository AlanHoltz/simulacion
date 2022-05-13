from random import random
import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as st
import statistics
from os import system
from tkinter import messagebox as mb
from random import randint


total_nros = 1500 #Cantidad de numeros a generar
total_corridas = 30


#DISTRIBUCIONES
def distribucion_uniforme(a,b): 
        return a + (b-a) * random()

def distribucion_exponencial(ex): 
    return -ex*math.log(random())

def distribucion_gamma(k,a): 
    tr = 1
    for i in range(0,k):
        tr *= random()

    return -math.log(tr)/a

def distribucion_normal(ex,stdx):   
    sum = 0

    for i in range(0,12):
        sum += random()

    return stdx * (sum - 6) + ex

def distribucion_pascal(k,q): 
    tr = 1
    qr = math.log(q)

    for i in range(0,k):
        tr *= random()

    return math.log(tr)/qr

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
    b = math.exp(-p)

    while tr > b:
        x += 1
        tr *= random()

    return x

def distribucion_empirica_discreta():
    x = 0
    p = [0.273, 0.037, 0.195, 0.009, 0.124, 0.058, 0.062, 0.151, 0.047, 0.044]
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
def grafica_dispersion(muestra):
    plt.figure('DISPERSIÓN')
    plt.title('Dispersión de los valores generados')
    plt.xlabel('')
    plt.ylabel('Valor')
    plt.plot(muestra, 'o', label='Dispersión de la primera corrida', color='orange')
    plt.show()

def grafica_histograma(muestra):
    plt.figure('HISTOGRAMA')
    plt.title('Histograma de frecuencias de los valores generados')
    plt.xlabel('Valor generado')
    plt.ylabel('Frecuencia absoluta')
    plt.hist(muestra, color='green', bins=25, alpha=0.5, edgecolor='black', linewidth=0.5)
    plt.show()

def grafica_densidad(muestra):
    data = pd.DataFrame(muestra) 
    data.plot.density(title='Funcion de Densidad de Probabilidad de los valores generados', legend=None, color='purple', linewidth=2) 
    plt.show()

def random_color():
    return "#" +  "%06x" % randint(0, 0xFFFFFF)

def grafica_promedios(distrib):
    promedios = []
    for i in range(total_corridas): 
        promedios.append(generador(distrib, False)) #Generador(False) devuelve el promedio de la tirada
    
    plt.figure('PROMEDIOS')
    plt.title('Evolución del promedio del conjunto de valores generados respecto a n')
    plt.suptitle('Numero de corridas: 30')
    plt.ylabel('Valor promedio de la corrida')
    plt.xlabel('Número de corridas')

    for k in promedios:
        plt.plot(k, color = random_color())
        
    plt.show()
    return promedios

def grafica_promedio_absoluto(promedios_corridas):
    promedio_abs = []
    for i in range(total_corridas): #30 
        promedio_abs.append(sum(promedios_corridas[i])/len(promedios_corridas[i])) 
    
    for i in range(total_nros):
        suma = 0
        for nro_corrida in range(total_corridas):
            suma += promedios_corridas[nro_corrida][i] 
        promedio_abs.append(suma/total_corridas)

    plt.figure('PROMEDIO')
    plt.title('Evolución del promedio del promedio del conjunto de valores generados respecto a n')
    plt.suptitle('Numero de corridas: 30')
    plt.plot(promedio_abs)
    plt.xlabel('Número de corridas')
    plt.ylabel('Valor promedio de la corrida')
    plt.show()


#PRUEBAS

def prueba_chi2_uniforme(numeros):
    k=round(math.sqrt(total_nros))
    pi=1/k 
    ei=total_nros*pi
    cantInt=round(total_nros/k)
    obsI=[]
    chiQ=[]
    ini=0
    fin=ini+ pi
    for i in range(cantInt):
        cont=0
        for x in range(total_nros):
            if (numeros[x]>ini and numeros[x]<=fin):
                cont+=1
        valor=((cont-ei)**2)/ei
        chiQ.append(valor)
        obsI.append(cont)
        ini=fin
        fin=fin+pi
    r=st.chi2.ppf(0.95 ,k-1)>sum(chiQ)
    if r:
        return("PRUEBA CHI2: Aprobada \n")
    else: 
        return("PRUEBA CHI2: Reprobada \n")

def prueba_chi2_exponencial(numeros):
    ei=[]
    chiQ=[]
    obsI=[]
    cantInt=0
    while 2**cantInt<=total_nros:
        cantInt+=1
    rango=max(numeros)-min(numeros)
    inter=rango/cantInt
    ini=0
    fin=ini+inter
    for i in range(cantInt):
        cont=0
        for x in range(total_nros):
            if (numeros[x]>ini and numeros[x]<=fin):
                cont+=1
        a=st.expon.cdf(ini,loc=0,scale=np.mean(numeros))
        b=st.expon.cdf(fin,loc=0,scale=np.mean(numeros))
        pi=len(numeros)*(b-a)
        ei.append(pi)
        valor=((cont-pi)**2)/pi
        chiQ.append(valor)
        obsI.append(cont)
        ini=fin
        fin=fin+inter
    r=st.chi2.ppf(0.95 ,cantInt-1)>sum(chiQ)
    if r:
        return("PRUEBA CHI2: Aprobada \n")
    else: 
        return("PRUEBA CHI2: Reprobada \n")
    
def prueba_chi2_poisson(numeros):
    pi=[]
    ei=[]
    k=max(numeros)
    for j in range(max(numeros)-1):
        n=st.poisson.pmf(j,0.5,0)
        pi.append(n)
    pi.append(1-sum(pi))
    for r in range(k):
        ei.append(total_nros*pi[r])
    obsI=[]
    chiQ=[]

    for i in range(k-1):
        cont=0
        for x in range(total_nros):
            if (numeros[x]==i):
                cont+=1
        valor=((cont-ei[i])**2)/ei[i]
        chiQ.append(valor)
        obsI.append(cont)
    r=st.chi2.ppf(0.95 ,k-1)>sum(chiQ)
    if r:
        return("PRUEBA CHI2: Aprobada \n")
    else: 
        return("PRUEBA CHI2: Reprobada \n")

def prueba_chi2_normal(numeros):
    rango=max(numeros)-min(numeros)
    cantInt=round(1+3.222*math.log10(total_nros))
    salto=rango/cantInt
    obsI=[]
    ei=[]
    chiQ=[]
    ini=min(numeros)
    fin=ini+salto
    for i in range(1,cantInt):
        cont=0
        for x in range(total_nros):
            if numeros[x]>=ini and numeros[x]<fin:
                cont+=1
        obsI.append(cont)
        a=st.norm.cdf(ini,loc=np.mean(numeros),scale=math.sqrt(np.var(numeros)))
        b=st.norm.cdf(fin,loc=np.mean(numeros),scale=math.sqrt(np.var(numeros)))
        v=total_nros*(b-a)
        ei.append(v)
        chi=((cont-v)**2)/v
        chiQ.append(chi)
        ini=fin
        fin+=salto
    r=st.chi2.ppf(0.95 ,cantInt-1)>sum(chiQ)
    if r:
        return("PRUEBA CHI2: Aprobada \n")
    else: 
        return("PRUEBA CHI2: Reprobada \n")

def prueba_chi2_binomial(numeros,n,p):
    pi=[]
    ei=[]
    k=max(numeros)
    for j in range(k):
        s=st.binom.pmf(j,n,p)
        pi.append(s)
    pi.append(1-sum(pi))
    for r in range(k):
        ei.append(total_nros*pi[r])
    obsI=[]
    chiQ=[]
    for i in range(k):
        cont=0
        for x in range(total_nros):
            if (numeros[x]==i):
                cont+=1
        valor=((cont-ei[i])**2)/ei[i]
        chiQ.append(valor)
        obsI.append(cont)
    r=st.chi2.ppf(0.95 ,k-1)>sum(chiQ)
    if r:
        return("PRUEBA CHI2: Aprobada \n")
    else: 
        return("PRUEBA CHI2: Reprobada \n")

def prueba_chi2_empirica(numeros):
    pi= [0.273, 0.037, 0.195, 0.009, 0.124, 0.058, 0.062, 0.151, 0.047, 0.044]
    cantInt=len(pi)
    ei=[]
    obsI=[]
    chiQ=[]
    for z in range(cantInt):
        s=total_nros*pi[z]
        ei.append(s)
    for i in range(cantInt):
        cont=0
        for x in range(total_nros):
            if numeros[x]==i:
                cont+=1
        valor=((cont-ei[i])**2)/ei[i]
        chiQ.append(valor)
        obsI.append(cont)
    r=st.chi2.ppf(0.95 ,cantInt-1)>sum(chiQ)
    if r:
        return("PRUEBA CHI2: Aprobada \n")
    else: 
        return("PRUEBA CHI2: Reprobada \n")

def prueba_corridas_media ():
    media_esperada = sum(numeros_generados)/total_nros
    Z = 1.96
    n1 = 0
    n2 = 0
    b = 1
    aux = ''

    for n in numeros_generados:
        if n < media_esperada:
            n1 += 1
            if aux == 'sobre':
                b += 1
            aux = 'bajo'
        else:
            n2 += 1
            if aux == 'bajo':
                b += 1
            aux = 'sobre'

    N = n1 + n2
    if N <= 1:
        estado = ('PRUEBA DE CORRIDAS ARRIBA/ABAJO DE LA MEDIA: Reprobada. Los numeros no son independientes. \n')

    else:
        media_test = (2 * n1 * n2 ) / (n1 + n2 ) +1
        varianza_test = (2 * n1 * n2 * (2 * n1 * n2 - N)) / (N ** 2 * (N - 1))
        if varianza_test != 0:
            z_muestra = (b - media_test) / math.sqrt(varianza_test)

            if z_muestra < Z:
                estado = ('PRUEBA DE CORRIDAS ARRIBA/ABAJO DE LA MEDIA: Aprobada. Los numeros son independientes.\n')
            else:
                estado = ('PRUEBA DE CORRIDAS ARRIBA/ABAJO DE LA MEDIA: Reprobada. Los numeros no son independientes.\n')
        else:
            estado = ('PRUEBA DE CORRIDAS ARRIBA/ABAJO DE LA MEDIA: Reprobada. Los numeros no son independientes.\n')
    
    return estado

def prueba_de_rachas():
    rachas, n1, n2 = 0, 0, 0
    media = statistics.median(numeros_generados)

    for i in range(total_nros):
        if (numeros_generados[i] >= media and numeros_generados[i - 1] < media) or \
                (numeros_generados[i] < media and numeros_generados[i - 1] >= media):
            rachas += 1

        if (numeros_generados[i]) >= media:
            n1 += 1
        else:
            n2 += 1
    rachas_esp = ((2 * n1 * n2) / (n1 + n2)) + 1  
    desv = math.sqrt((2 * n1 * n2 * (2 * n1 * n2 - n1 - n2)) / (((n1 + n2) ** 2) * (n1 + n2 - 1)))
    Z = (rachas - rachas_esp) / desv

    if (Z > -1.96 and Z < 1.96):  # Para un nivel de confianza del 95%
        return("PRUEBA DE RACHAS: Aprobada. Los numeros son aleatorios \n")
    else:
        return("PRUEBA DE RACHAS: Reprobada. Los numeros no son aleatorios \n")



def generador(dis, flag):
    numeros_generados = []
    promedio_corrida = []
    chi2 = ""
    
    if (dis == 1):
        for i in range(total_nros):
            numeros_generados.append(distribucion_uniforme(1,100)) 
            promedio_corrida.append(sum(numeros_generados)/len(numeros_generados))
        nombre = ("-- DISTRIBUCION UNIFORME -- \n Parametros a: 1 , b: 100\n\n")
        chi2 = prueba_chi2_uniforme(numeros_generados)

    if (dis == 2):
        for i in range(total_nros):
            numeros_generados.append(distribucion_exponencial(1)) 
            promedio_corrida.append(sum(numeros_generados)/len(numeros_generados))
        nombre = ("-- DISTRIBUCION EXPONENCIAL -- \n Parametro ex: 1\n\n")
        chi2 = prueba_chi2_exponencial(numeros_generados)
        
    if (dis == 3):
        for i in range(total_nros):
            numeros_generados.append(distribucion_gamma(1,2)) 
            promedio_corrida.append(sum(numeros_generados)/len(numeros_generados))
        nombre = ("-- DISTRIBUCION GAMMA -- \n Parametros k: 1 , a: 2\n\n")
        
    if (dis == 4):
        for i in range(total_nros):
            numeros_generados.append(distribucion_normal(0,1)) 
            promedio_corrida.append(sum(numeros_generados)/len(numeros_generados))
        nombre = ("-- DISTRIBUCION NORMAL -- \n Parametros ex: 0 , stdx: 1\n\n")
        chi2 = prueba_chi2_normal(numeros_generados)
        
    if (dis == 5):
        for i in range(total_nros):
            numeros_generados.append(distribucion_pascal(20,0.4))
            promedio_corrida.append(sum(numeros_generados)/len(numeros_generados)) 
        nombre = ("-- DISTRIBUCION PASCAL -- \n Parametros k: 20 , q: 0.4\n\n")
        
    if (dis == 6):
        for i in range(total_nros):
            numeros_generados.append(distribucion_binomial(20,0.4)) 
            promedio_corrida.append(sum(numeros_generados)/len(numeros_generados))
        nombre = ("-- DISTRIBUCION BINOMIAL -- \n Parametros n: 20 , p: 0.4\n\n")
        chi2 = prueba_chi2_binomial(numeros_generados, 20, 0.4)
        
    if (dis == 7):
        for i in range(total_nros):
            numeros_generados.append(distribucion_hipergeometrica(1000,150,0.5)) 
            promedio_corrida.append(sum(numeros_generados)/len(numeros_generados))
        nombre = ("-- DISTRIBUCION HIPERGEOMETRICA -- \n Parametros tn: 1000, ns: 150, p: 0.5 \n\n")
        
    if (dis == 8):
        for i in range(total_nros):
            numeros_generados.append(distribucion_poisson(10)) 
            promedio_corrida.append(sum(numeros_generados)/len(numeros_generados))
        nombre = ("-- DISTRIBUCION DE POISSON -- \n Parametro p: 10\n\n")
        chi2 = prueba_chi2_poisson(numeros_generados)
        
    if (dis == 9):
        for i in range(total_nros):
            numeros_generados.append(distribucion_empirica_discreta()) 
            promedio_corrida.append(sum(numeros_generados)/len(numeros_generados))
        nombre = ("-- DISTRIBUCION EMPIRICA DISCRETA -- \n\n")
        chi2 = prueba_chi2_empirica(numeros_generados)
    
    if flag: #True para calculos iniciales-False para promedios
        return(numeros_generados, nombre, chi2)
    else:
        return(promedio_corrida)


#MAIN
op=0
while(op<1 or op>9):
    system("cls")
    print("\n-- SELECCIONE DISTRIBUCION: --")
    print(" 1 - UNIFORME \n 2 - EXPONENCIAL \n 3 - GAMMA \n 4 - NORMAL \n 5 - PASCAL \n 6 - BINOMIAL \n 7 - HIPERGEOMÉTRICA \n 8 - POISSON \n 9 - EMPIRICA DISCRETA")
    op = int(input("\n opción: "))
    if(op<1 or op>9): print("Ingrese un numero entre 1 y 9.\n")

numeros_generados, distribucion, resultado_chi2 = generador(op, True) #True para calculos iniciales-False para promedios
rachas = prueba_de_rachas()
corridas_media = prueba_corridas_media()

grafica_dispersion(numeros_generados)
grafica_histograma(numeros_generados)
grafica_densidad(numeros_generados)
proms = grafica_promedios(op)
grafica_promedio_absoluto(proms)

mensaje = distribucion + resultado_chi2 + rachas + corridas_media
mb.showinfo(title="Resultado de pruebas", message=mensaje)








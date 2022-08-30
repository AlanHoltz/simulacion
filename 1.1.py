from random import randint
from turtle import color
import numpy as np
import matplotlib.pyplot as plt
from os import system

NUMERO_CORRIDAS = 15 #20
NUMERO_TIRADAS = 1000 #1000
NUMERO_RULETA = 36
ELEGIDOS = [12,18,27]

corridas = []

def random_color():
    return "#" +  "%06x" % randint(0, 0xFFFFFF)



def grafica_promedios():
    plt.figure('PROMEDIOS')
    plt.title('Evolución del promedio del conjunto de valores obtenidos respecto a n')
    plt.suptitle('Numero de corridas: '+ str(NUMERO_CORRIDAS))

    for corrida in corridas:
        plt.plot(corrida["promedios"], color = random_color())
    
    prom_esp = NUMERO_RULETA / 2
    plt.axhline(prom_esp, label='Esperanza esperada', color = "black")
    plt.xlabel('Número de tiradas')
    plt.ylabel('Valor promedio de las tiradas')
    plt.ylim(10,26)
    plt.legend()
    plt.show()



def grafica_promedio_gral():
    plt.figure('PROMEDIO GENERAL')
    plt.title('Evolución del promedio del conjunto de promedios respecto a n')

    prom_esp = NUMERO_RULETA / 2
    plt.axhline(prom_esp, label='Esperanza esperada', color = "black")

    prom_gral = []
    for nro_tirada in range(NUMERO_TIRADAS):
        suma = 0
        for corrida in corridas:
            suma += corrida["promedios"][nro_tirada] #Acumulo la suma de los 30 promedios de cada tirada
        prom_gral.append(suma/NUMERO_CORRIDAS)
    plt.plot(prom_gral, label='Esperanza promedio' )
    
    plt.xlabel('Número de tiradas')
    plt.ylabel('Valor promedio de las tiradas')
    plt.ylim(10,26)
    plt.legend()
    plt.show()



def grafica_desvios():
    plt.figure('DESVIOS')
    plt.title('Evolución del desvío del conjunto de valores obtenidos respecto a n')
    plt.suptitle('Numero de corridas: '+ str(NUMERO_CORRIDAS))

    for corrida in corridas:
        plt.plot(corrida["desvios"], color = random_color())

    desv_esp = np.std(tiradas)
    plt.xlabel('Número de tiradas')
    plt.ylabel('Valor del desvío')
    plt.ylim(4,16)
    plt.axhline(desv_esp, label='Desvio esperado', color = "black") 
    plt.legend()
    plt.show()



def grafica_desvio_gral():
    plt.figure('DESVIO GENERAL')
    plt.title('Evolución del promedio del conjunto de desvíos respecto a n')

    desv_gral = []
    for nro_tirada in range(NUMERO_TIRADAS):
        suma = 0
        for corrida in corridas:
            suma += corrida["desvios"][nro_tirada] 
        desv_gral.append(suma/NUMERO_CORRIDAS)
    plt.plot(desv_gral, label='Desvío promedio' )

    desv_esp = np.std(tiradas)
    plt.xlabel('Número de tiradas')
    plt.ylabel('Valor del desvío')
    plt.ylim(4,16)
    plt.axhline(desv_esp, label='Desvio esperado', color = "black") 
    plt.legend()
    plt.show()



def grafica_varianza():
    plt.figure('VARIANZA')
    plt.title('Evolución de la varianza del conjunto de valores obtenidos respecto a n')
    plt.suptitle('Numero de corridas: '+ str(NUMERO_CORRIDAS))

    for corrida in corridas:
        plt.plot(corrida["varianzas"], color = random_color())

    var_esp = np.var(tiradas)
    plt.xlabel('Número de tiradas')
    plt.ylabel('Valor de la varianza')
    plt.ylim(1,200)
    plt.axhline(var_esp, label='Varianza esperada', color = "black")
    plt.legend()
    plt.show()



def grafica_varianza_gral():
    plt.figure('VARIANZA GENERAL')
    plt.title('Evolución del promedio del conjunto de varianzas respecto a n')

    var_gral = []
    for nro_tirada in range(NUMERO_TIRADAS):
        suma = 0
        for corrida in corridas:
            suma += corrida["varianzas"][nro_tirada] 
        var_gral.append(suma/NUMERO_CORRIDAS)
    plt.plot(var_gral, label='Varianza promedio' )

    var_esp = np.var(tiradas)
    plt.xlabel('Número de tiradas')
    plt.ylabel('Valor de la varianza')
    plt.ylim(1,200)
    plt.axhline(var_esp, label='Varianza esperada', color = "black") 
    plt.legend()
    plt.show()    



def grafica_frecuencia_relativa(num):
    plt.figure('FRECUENCIA RELATIVA')
    plt.title(f'Evolución de la Frecuencia Relativa para {num} respecto a n')
    plt.suptitle('Numero de corridas: '+ str(NUMERO_CORRIDAS))
    
    for corrida in corridas:
        plt.plot(corrida["frecuencias"][num], color = random_color())
    
    fr_esp = 1/(NUMERO_RULETA+1)
    plt.xlabel('Número de tiradas')
    plt.ylabel('Valor de la frecuencia relativa')
    plt.ylim(0,0.3)
    plt.axhline(fr_esp, label='Frecuencia relativa esperada', color = "black") 
    plt.legend()
    plt.show()



def grafica_frecuencia_relativa_gral(num):
    plt.figure('FRECUENCIA RELATIVA')
    plt.title(f'Evolución del promedio de la frecuencia Relativa para {num} respecto a n')
    
    fr_gral = []
    for nro_tirada in range(NUMERO_TIRADAS):
        suma = 0
        for corrida in corridas:
            suma += corrida["frecuencias"][num][nro_tirada] 
        fr_gral.append(suma/NUMERO_CORRIDAS)
    plt.plot(fr_gral, label='Frecuencia relativa promedio' )
    
    var_esp = 1/(NUMERO_RULETA+1)
    plt.xlabel('Número de tiradas')
    plt.ylabel('Valor de la frecuencia relativa')
    plt.ylim(0,0.3)
    plt.axhline(var_esp, label='Frecuencia relativa esperada', color = "black") 
    plt.legend()
    plt.show()



def grafica_dispersion():
    plt.figure('DISPERSIÓN')
    plt.title('Dispersión de los valores de la primera corrida')
    plt.xlabel('Número de tiradas')
    plt.ylabel('Número de la ruleta')
    plt.plot(corridas[0]["tiradas"], 'o', label='Dispersión de la primera corrida', color='orange')
    plt.show()



def grafica_histograma():
    plt.figure('HISTOGRAMA')
    plt.title('Histograma de frecuencias de la primera corrida')
    plt.xlabel('Número de la ruleta')
    plt.ylabel('Frecuencia absoluta')
    plt.hist(corridas[0]["tiradas"], color='green')
    plt.show()

#MAIN

system("cls")


for i in range(1, NUMERO_CORRIDAS + 1):

    contadores = {12: 0, 18: 0, 27: 0}
    frecuencias = {12: [], 18: [], 27: []}
    tiradas = []
    desvios = []
    varianzas = []
    promedios = []

    for j in range(1,NUMERO_TIRADAS+1):      #POR CADA TIRADA SE GUARDA SU PROMEDIO,VARIANZA Y DESVÍO ACTUAL
        
        tiradas.append(randint(0,NUMERO_RULETA))
        promedios.append(sum(tiradas)/j)
        varianzas.append(np.var(tiradas))
        desvios.append(np.std(tiradas))
        
        for elegido in ELEGIDOS:    #SE GUARDA LA ÚLTIMA FRECUENCIA ALMACENADA DE CADA ELEGIDO(EN CASO DE QUE TODAVÍA
                                    #EL ARRAY NO CONTENGA NADA SE GUARDA 0)
            
            if len(frecuencias[elegido]) > 0:
                frecuencias[elegido].append(frecuencias[elegido][-1])

            else:
                frecuencias[elegido].append(0)
        
        if(tiradas[j-1] in ELEGIDOS):   #SE PISA EL ÚLTIMO VALOR DEL ARRAY DE FRECUENCIAS SI EL NÚMERO ES UNO DE LOS ELEGIDOS

            contadores[tiradas[j-1]] += 1
            frecuencias[tiradas[j-1]][-1] = contadores[tiradas[j-1]]/j 

    corridas.append({
        "promedios": promedios,
        "desvios" : desvios,
        "varianzas": varianzas,
        "tiradas": tiradas,
        "frecuencias": frecuencias
    })



#GRAFICAS 
grafica_frecuencia_relativa(12)
grafica_frecuencia_relativa_gral(12)
grafica_frecuencia_relativa(18)
grafica_frecuencia_relativa_gral(18)
grafica_frecuencia_relativa(27)
grafica_frecuencia_relativa_gral(27)

grafica_promedios()
grafica_promedio_gral()
grafica_desvios()
grafica_desvio_gral()
grafica_varianza()
grafica_varianza_gral()

grafica_dispersion()
grafica_histograma()
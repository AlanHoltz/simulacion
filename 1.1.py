from random import randint
import numpy as np
import matplotlib.pyplot as plt
from os import system

NUMERO_CORRIDAS = 5
NUMERO_TIRADAS = 1000
NUMERO_RULETA = 36
ELEGIDOS = [12,18,27]

corridas = []

def random_color():
    return "#" +  "%06x" % randint(0, 0xFFFFFF)

def grafica_promedios():
    plt.figure('PROMEDIOS')
    plt.title('Evolución del Promedio')

    for k,corrida in enumerate(corridas):
        plt.plot(corrida["promedios"], color = random_color(), label= f'{k + 1}° Corrida')

    prom_esp = NUMERO_RULETA / 2
    plt.axhline(prom_esp, label='Promedio esperado')
    plt.xlabel('Número de tiradas')
    plt.ylabel('Valor promedio de las tiradas')
    plt.legend()
    plt.show()

def grafica_desvios():
    plt.figure('DESVIOS')
    plt.title('Evolución del Desvío')

    for k,corrida in enumerate(corridas):
        plt.plot(corrida["desvios"], color = random_color(), label= f'{k + 1}° Corrida')

    desv_esp = np.std(tiradas)
    plt.xlabel('Número de tiradas')
    plt.ylabel('Valor del desvío')
    plt.axhline(desv_esp, label='Desvio esperado') 
    plt.legend()
    plt.show()

def grafica_varianza():
    plt.figure('VARIANZA')
    plt.title('Evolución de la Varianza')

    for k,corrida in enumerate(corridas):
        plt.plot(corrida["varianzas"], color = random_color(), label= f'{k + 1}° Corrida')

    var_esp = np.var(tiradas)
    plt.xlabel('Número de tiradas')
    plt.ylabel('Valor de la varianza')
    plt.axhline(var_esp, label='Varianza esperada')
    plt.legend()
    plt.show()

def grafica_frecuencia_relativa(num):
    plt.figure('FRECUENCIA RELATIVA')
    plt.title(f'Evolución de la Frecuencia Relativa para {num}')
    
    for k,corrida in enumerate(corridas):
        plt.plot(corrida["frecuencias"][num], color = random_color(), label= f'{k + 1}° Corrida')
    
    var_esp = 1/(NUMERO_RULETA+1)
    plt.xlabel('Número de tiradas')
    plt.ylabel('Valor de la frecuencia relativa')
    plt.axhline(var_esp, label='Frecuencia relativa esperada') 
    plt.legend()
    plt.show()

def grafica_dispersion():
    plt.figure('DISPERSIÓN')
    plt.title('Dispersión de los valores de la primera corrida')
    plt.xlabel('Número de tiradas')
    plt.ylabel('Número de la ruleta')
    plt.plot(corridas[0]["tiradas"], 'o', label='Dispersión de la primera corrida')
    plt.show()

def grafica_histograma():
    plt.figure('HISTOGRAMA')
    plt.title('Histograma de frecuencias de la primera corrida')
    plt.xlabel('Número de la ruleta')
    plt.ylabel('Frecuencia absoluta')
    plt.hist(corridas[0]["tiradas"])
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
        "desvios" :desvios,
        "varianzas": varianzas,
        "tiradas": tiradas,
        "frecuencias": frecuencias
    })




grafica_frecuencia_relativa(12)
grafica_frecuencia_relativa(18)
grafica_frecuencia_relativa(27)
grafica_promedios()
grafica_desvios()
grafica_varianza()
grafica_dispersion()
grafica_histograma()




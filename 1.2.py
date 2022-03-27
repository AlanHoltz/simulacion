import matplotlib.pyplot as plt
from os import system
from random import randint

ruleta = {
    0: "V", 1: "R", 2: "N", 3: "R", 4: "N", 5: "R", 6: "N", 7: "R", 8: "N", 9: "R", 10: "N", 11: "N", 12: "R", 13: "N",
    14: "R", 15: "N", 16: "R", 17: "N", 18: "R", 19: "R", 20: "N", 21: "R", 22: "N", 23: "R", 24: "N", 25: "R", 26: "N",
    27: "R", 28: "N", 29: "N", 30: "R", 31: "N", 32: "R", 33: "N", 34: "R", 35: "N", 36: "R"
}

CAPITAL_INICIAL = 1000
MONTO_APUESTA_INICIAL = 100


def grafica_flujo_caja(fc):
    plt.figure('FLUJO DE CAJA')
    plt.title('Evolución del flujo de caja respecto a n')
    plt.plot(fc, 'r-', label='Flujo de caja')
    plt.xlabel('Número de tiradas')
    plt.ylabel('Cantidad de capital')
    plt.axhline(CAPITAL_INICIAL, label='Flujo de caja inicial')
    plt.legend()
    plt.show()


def grafica_flujo_caja_poblacion(poblacion):
    plt.figure('FLUJO DE CAJA')
    for i in range(0, len(poblacion)):
        plt.plot(poblacion[i])
    plt.title('Evolución del flujo de caja respecto a n para una poblacion')
    #  plt.plot(fc, 'r-', label='Flujo de caja')
    plt.xlabel('Número de tiradas')
    plt.ylabel('Cantidad de capital')
    plt.axhline(CAPITAL_INICIAL, label='Flujo de caja inicial')
    plt.legend()
    plt.grid()
    plt.show()


def grafica_frecuencia(fr):
    plt.figure('FRECUENCIA')
    plt.title('Evolución de la frecuencia relativa de la obtencion la respuesta favorable respecto a n')
    plt.bar(range(len(fr)), fr)
    plt.xlabel('Número de tiradas')
    plt.ylabel('Frecuencia relativa')
    plt.show()


def grafica_torta(rojo, total):
    plt.figure('COLOR')
    plt.title('Distribucion del color de los valores obtenidos en la ruleta en n tiros')
    plt.pie(x=[rojo, total - rojo], colors=['red', 'grey'], labels=["ROJO", "NEGRO"], autopct='%1.2f%%')
    plt.show()


def martingala():
    flujo_caja = []
    frecuencia = []
    global CAPITAL_INICIAL
    global MONTO_APUESTA_INICIAL
    capital = CAPITAL_INICIAL
    monto_apuesta = MONTO_APUESTA_INICIAL
    color_apostado = "R"
    i = 0
    favorables = 0

    while capital >= monto_apuesta:
        tiro = randint(0, 36)
        if (ruleta[tiro] == color_apostado):
            capital += monto_apuesta
            monto_apuesta = MONTO_APUESTA_INICIAL
            favorables += 1
        else:
            capital -= monto_apuesta
            monto_apuesta *= 2

        i += 1

        frecuencia.append(favorables / i)
        flujo_caja.append(capital)

    print(frecuencia)
    grafica_flujo_caja(flujo_caja)
    grafica_frecuencia(frecuencia)
    grafica_torta(favorables, i)


def fibonacci():
    flujo_caja = []
    frecuencia = []
    global CAPITAL_INICIAL
    global MONTO_APUESTA_INICIAL
    capital = CAPITAL_INICIAL
    monto_apuesta = MONTO_APUESTA_INICIAL
    color_apostado = "R"
    i = 0
    favorables = 0
    monto_prev = 0

    while capital >= monto_apuesta:
        tiro = randint(0, 36)
        if (ruleta[tiro] == color_apostado):
            capital += monto_apuesta
            monto_apuesta = MONTO_APUESTA_INICIAL
            favorables += 1
        else:
            capital -= monto_apuesta
            monto_apuesta += monto_prev
            monto_prev = monto_apuesta

        i += 1

        frecuencia.append(favorables / i)
        flujo_caja.append(capital)


    grafica_flujo_caja(flujo_caja)
    grafica_frecuencia(frecuencia)
    grafica_torta(favorables, i)

def fibonacci_poblacion():
    flujo_caja = []
    frecuencia = []
    poblacion = []

    global CAPITAL_INICIAL
    global MONTO_APUESTA_INICIAL
    capital = CAPITAL_INICIAL
    monto_apuesta = MONTO_APUESTA_INICIAL
    color_apostado = "R"
    i = 0

    favorables = 0
    monto_prev = 0
    for i in range(0, 100):
        while capital >= monto_apuesta:
            tiro = randint(0, 36)
            if (ruleta[tiro] == color_apostado):
                capital += monto_apuesta
                monto_apuesta = MONTO_APUESTA_INICIAL
                favorables += 1
            else:
                capital -= monto_apuesta
                monto_apuesta += monto_prev
                monto_prev = monto_apuesta
            i += 1

            frecuencia.append(favorables / i)
            flujo_caja.append(capital)

        poblacion.append(flujo_caja)
        flujo_caja = []
        capital = CAPITAL_INICIAL
        monto_apuesta = MONTO_APUESTA_INICIAL
        color_apostado = "R"
        favorables = 0
        monto_prev = 0

    grafica_flujo_caja_poblacion(poblacion)


system("cls")
fibonacci()
fibonacci_poblacion()
martingala()

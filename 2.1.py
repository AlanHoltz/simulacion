import statistics
import matplotlib.pyplot as plt
from os import system
from random import randint

def generador_GCL():
    numeros = []
    m = (2**31)-1 # modulo
    a = 7**5  # multiplicador
    c = 5 # Incremento
    semilla = 885
    numeros.append(semilla)

    for i in range(1, 100):
        nro = (a * numeros[i - 1] + c) % m
        numeros.append(nro)
    print(numeros)
    return numeros

def generador_pmc():
    seed = 6923
    n = 100  # cantidad de numeros generados
    numeros = [seed]
    sem = []
    sem2 = []
    for i in range(1, n):
        x = numeros[i - 1] ** 2
        print(x)
        if (len(str(x)) < 8):
            print("antes:", x)
            x = completa_ceros(x)
            print("desp:", x)
        sem = [int(a) for a in str(x)]
        sem2 = sem[2:6]
        seed = int(''.join(map(str, sem2)))
        numeros.append(seed)
    print("Numeros:     ", numeros)


def completa_ceros(sem):
    sem = str(sem)
    for i in range(0, (8 - len(sem))):
        sem = '0' + sem
    return sem


def aboveandbelow():
    n1 = []  # Numeros por encima de la media
    n2 = []  # Numeros por debajo de la media
    rtot = 0
    med = statistics.median(generador_GCL())
    for x in generador_GCL():
        rtot += x
        if x > med:
            n1.append(x)
        else:
            n2.append(x)
    r = 100
    n1l = len(n1)
    n2l = len(n2)
    promR = (2 * n1l *n2l) /(n1l + n2l) + 1

    devR = ((2 * n1l * n2l)*((2 * n1l * n2l) - n1l - n2l))/(((n1l + n2l)**2)*(n1l + n2l - 1))
    Z = (r - promR)/devR
    print (Z)

# generador_pmc()
aboveandbelow()

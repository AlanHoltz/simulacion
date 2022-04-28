import statistics
import matplotlib.pyplot as plt
from os import system
from random import randint
import math
import statistics


def generador_GCL():
<<<<<<< Updated upstream
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
=======
        global numeros
        m = 2**48 #modulo
        a = 25214903917  #multipliador
        c = 11 #Incremento
        semilla = 14758
        numeros.append(semilla)

        for i in range(1,100):
            nro = (a*numeros[i-1] + c) % m
            numeros.append(nro)
        print("GCL:     ",numeros)
>>>>>>> Stashed changes

def generador_pmc():
    global numeros
    seed = 6923
<<<<<<< Updated upstream
    n = 100  # cantidad de numeros generados
=======
    n=100#cantidad de numeros generados
>>>>>>> Stashed changes
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

def test_rachas():
    media = statistics.median(numeros)
    Z = abs(prueba_de_rachas(numeros, media))
    print(Z)
    if (Z > 1.96): #Para un nivel de confianza del 95% --> Zcritico = 0.025
        print("Los numeros no son aleatorios ")
    else:
        print("Los numeros son aleatorios ")

<<<<<<< Updated upstream
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
=======
def prueba_de_rachas(numeros, media):
    rachas, n1, n2 = 0, 0, 0

    
    for i in range(len(numeros)):

        if (numeros[i] >= media and numeros[i - 1] < media) or \
                (numeros[i] < media and numeros[i - 1] >= media):
            rachas += 1

        if (numeros[i]) >= media:
            n1 += 1
        else:
            n2 += 1
    rachas_esp = ((2 * n1 * n2) / (n1 + n2)) + 1 #Número de corridas esperadas
    desv = math.sqrt((2 * n1 * n2 * (2 * n1 * n2 - n1 - n2)) / (((n1 + n2) ** 2) * (n1 + n2 - 1))) # Desviación estándar del número de carreras

    z = (rachas - rachas_esp) / desv

    return z
numero = "55344"
poker = []
c = 0

for i in numero:
    compara = i
    for j in range(0,5):
        if compara == numero[j]:
            c+= 1
        print ('j= ', j, ' compara: ', compara, numero[j])
    poker.append(c)
    c = 0
print (poker)

numeros=[]
#generador_pmc()
generador_GCL()
test_rachas()
>>>>>>> Stashed changes

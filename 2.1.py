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


def prueba_poker():
    c = 0
    p2, p1, f, po, q, pa, t = 0, 0, 0, 0, 0, 0, 0
    esperada = []
    probabilidad = []
    observada = []
    fila = []
    columna = []
    que_hay = []
    lista_nueva = [[4, 0, 6, 5, 1],[4, 0, 6, 5, 1],[4, 0, 6, 5, 1],[4, 0, 6, 5, 1],[7, 7, 9, 5, 8],[7, 7, 2, 2, 9],[0, 0, 9, 9, 9], [2, 2, 2, 2, 6], [0, 0, 0, 0, 0],
                   [6, 6, 6, 2, 1],[6, 6, 6, 2, 1],[6, 6, 6, 2, 1]]
    n = len(lista_nueva)
    for i in range(0,len(lista_nueva)):
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
    for i in range(0,7):
        x = ((esperada[i]*observada[i])**2)/esperada[i]
    print(x)
    chi_cuadrado = 12.5916
    if x<= chi_cuadrado:
        print("No se puede rechazar que los numeros son independientes")


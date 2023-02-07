#Proyecto donde la computadora te adivina el numero en el que estas pensado
import random 
from time import sleep
Ador, Titulo = "","Te adivino el numero"
#Adornat Titulo
print(f"{Ador.center(50,'*')}")
print(f"{Titulo.center(50).upper()}")
print(f"{Ador.center(50,'*')}")

print(f"\nPiensa en un numero del 1 al 10 \nTines 5 segundos para pensar")

#bloque para que adivine el numero
def adivina():
    delay = 5
    x = random.randrange(1,10)
    sleep(delay)
    print(f"Estabas pensado en el numero: {x}... ")
    SN = input("S/N: ")
    if SN.upper() == 'S':
        print(f"\nEeeeeeeee GANE\nEl numero en el que pensaste era: {x}.")
    else: 
        #Bloque de comprobacion
        bA = input("Tu numero era mas alto o mas bajo: ")
        if bA.upper() == "ALTO":
            while True:
                x +=1
                SN = input(f"Tu numero es: {x} S/N: ")
                if SN.upper() == "N":
                    continue
                else:
                    print(f"\nEeeeeeeee GANE\nEl numero en el que pensaste era: {x}.")
                    break
        elif bA.upper() == "BAJO":
            while True:
                x -=1
                SN = input(f"Tu numero es: {x} S/N: ")
                if SN.upper() == "N":
                    continue
                else:
                    print(f"\nEeeeeeeee GANE\nEl numero en el que pensaste era: {x}.")
                    break


adivina()
import time

pos = True
cont = 0

while pos:
        print(" " * cont + "*****")
        cont += 1
        time.sleep(0.5)
        if cont == 10:
            pos = False
    
while not pos:
        print(" " * cont + "*****")
        cont -= 1
        time.sleep(0.5)
        if cont == 0:
            pos = True

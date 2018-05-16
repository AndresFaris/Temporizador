import time
from IPython.display import clear_output

print ("\t TEMPORIZADOR")
print("ingresa el tiempo que tienes(Si no tienes ingresa el valor de cero(0)): ")
H=int(input("Horas:"))
M=int(input("Minutos:"))
S=int(input("Segundos: "))

if (H!=0 or M!=0 or S!=0):
    for h in range(H,-1,-1):
        for m in range(M,-1,-1):
            for s in range(S,0,-1):
                print("Hora:",h,"Min:",m,"Seg:",s)
                time.sleep(1)
                clear_output()
            S=60
        M=60

               
           
    
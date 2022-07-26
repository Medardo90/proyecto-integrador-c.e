import random
f=3
c=3
sumaColu=0
sumaFila=0
suma1=0
lista=[]
while f>30 or f<4:
    f=int(input("Ingrese la cantidad de filas (4-30): "))
while c>30 or c<4:
    c=int(input("Ingrese la cantidad de columnas (4-30): "))
colu=[0]*c
for i in range(f):
    lista.append([])
    for j in range(c):
        lista[i].append(random.randint(0,10))
for i in range(f):
    sumaF=0
    for j in range(c):
        print(f"{lista[i][j]:3d}",end=" ")
        sumaF+=lista[i][j]
        suma1+=lista[i][j]
        colu[j]+=lista[i][j]
    print(f"| {sumaF:3d}")
    sumaFila+=sumaF
print("-"*30)
for i in range(c):
    print(f"{colu[i]:3d}",end=" ")
    sumaColu+=colu[i]   
print(f"\nEl promedio de la suma de las filas es: {(sumaFila/f):.2f}\nEl promedio de la suma de las columnas es: {(sumaColu/c):.2f}")
print(f"El promedio de la matriz es: {(suma1/(f*c)):.2f}")

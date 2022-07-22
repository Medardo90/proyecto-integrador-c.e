


import random

salir = 'N'
while salir != 'S':
  #==== INGRESAR FILA Y COLUMNA ======
  filas = int(input('Ingrese la cantidad de materias: '))
  while filas < 1 or filas > 10:
    print('Error, la fila debe debe estar entre 1 y 10!')
    filas = int(input('Ingrese la cantidad de materias: '))

  columnas = int(input('Ingrese la cantidad de notas: '))
  while columnas < 1 or columnas > 7:
    print('Error, la fila debe debe estar entre 1 y 10!')
    columnas = int(input('Ingrese la cantidad de notas: '))

  #======= DELCARAR LA MATRIZ Y MATERIAS ======
  matriz = []
  materias = []

  #===== INGRESAR LAS MATERIAS ======
  for i in range(filas):
    materias.append(f'Ingrese la materia {i+1}: ')


  opcion = int(input('Dese ingresar las notas de: \n[1] Manualmente\n[2] Aletoriamente\nOpcion: '))
  if opcion == 1:
    #==== INGRESAR LAS NOTAS MANUALMENTE ======
    for i in range(filas):
      notas = []
      print(f'Notas de la materia {materias[i]}')
      for j in range(columnas):
        nota = int(input(f'Nota {j+1}: '))
        while nota < 0 or nota > 10:
          print('Error la nota debe estar entre 0 y 10!')
          nota = int(input(f'Nota {j+1}: '))
        notas.append(nota)
      
      matriz.append(notas)
  else:
    for i in range(filas):
      notas = []
      for j in range(columnas):
        nota = random.randint(0,10)
        notas.append(nota)
    
      matriz.append(notas)

  # Ingresamos el indice de la materia
  opcion = 0
  while opcion < 0 or opcion > filas:
    for i in range(filas):
      print(f'[{i+1}] {materias[i]}')
    opcion = int(input('Ingres el indice de la materia para realizar el reporte: '))

  # Calculamos el promedio de la materia
  promedioMateria = sum(matriz[opcion]) / columnas
  promedioMateria = round(promedioMateria, 2)
  print(f'Promedio de {materias[opcion]}: {promedioMateria}')

  #Calculamos la nota minima de maxima de la materia escojida
  notaMinima = matriz[opcion][0]
  notaMaxima = matriz[opcion][0]

  for j in range(columnas):
    if notaMinima > matriz[opcion][j]:
      notaMinima = matriz[opcion][j]
    if notaMaxima < matriz[opcion][j]:
      notaMaxima = matriz[opcion][j]
  
  print(f'Nota mínima: {notaMinima}')
  print(f'Nota maxima: {notaMaxima}')

  # Calcular el promedio general
  suma = 0
  for i in range(filas):
    s = 0
    for j in range(columnas):
      s += matriz[i][j]
    suma += s / columnas
  
  promedio = round(suma/filas, 2)

  if promedio > promedioMateria:
    print(f'El promedio de la materia ({promedioMateria}) está por debajo del promedio general ({promedio})')
  else:
    print(f'El promedio de la materia ({promedioMateria}) está por encima del promedio general ({promedio})')

  salir = input('Salir si(S) / no(N): ').upper()

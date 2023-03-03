# Print array
def imprimir_Arreglo(arreglo):
  tamanio = len(arreglo)
  for i in range(tamanio-1):
    print(f' [ {arreglo[i]} ] ',end="")

#Print array organized
def algoritmo_Burbuja(arreglo):
  for i in range(len(arreglo) - 1):
    for j in range(len(arreglo) - 1 - i):
      if arreglo[j] > arreglo[j + 1]:
        aux = arreglo[j]
        arreglo[j] = arreglo[j + 1]
        arreglo[j + 1] = aux

      
listasuelditos = [20.8,150.5,170.5,180.8,190,30,75.6,200]

print("\n Suelo de empleados sin ordenar with for\n")
imprimir_Arreglo(listasuelditos)

algoritmo_Burbuja(listasuelditos)
print("\n\n Suelo de empleados ordenado with for\n")
imprimir_Arreglo(listasuelditos)

def imprimir_Arreglo(array):
  tamanio = len(array)
  for i in range(tamanio-1):
    print(f' [ {array[i]} ] ', end = "")

def algoritmo_bur_while(array):
  num = len(array)
  i = 0
  while i < num:
    j = i
    while j < num:
      if array[i] > array[j]:
        aux = array[i]
        array[i] = array[j]
        array[j] = aux
      j = j + 1
    i = i + 1

listaSueldos = [20.8,150.5,170.5,180.8,190,30,75.6,200]

print("\n Suelo de empleados sin ordenar with for\n")
imprimir_Arreglo(listaSueldos)

algoritmo_bur_while(listaSueldos)
print("\n\n Suelo de empleados ordenado with while\n")
imprimir_Arreglo(listaSueldos)
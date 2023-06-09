import numpy as np

arr = np.random.randint(0, 101, size=(3, 3))
print(arr)

suma = 0
mayor = 0
menor = 101

for i in range(3):
    for j in range(3):
        suma += arr[i][j]
        if mayor < arr[i][j]:
            mayor = arr[i][j]
        if menor > arr[i][j]:
            menor = arr[i][j]
        if not (i == j) and not (i + j == 2):
            arr[i][j] = 0
print(f"Suma de elementos: {suma}")
print(f"Elemento Mayor: {mayor}")
print(f"Elemento Menor: {menor}")
print(f"Promedio: {suma/9}")
print(arr)
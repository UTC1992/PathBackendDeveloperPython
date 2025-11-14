import copy

numbers_list = [1, 2, -10, 3, 22, -8, 4, 0, 10, -2]

def change_value(numbers_aux):
    numbers_aux[0] = 6
    print(numbers_aux)

# change_value(numbers_list)
print(numbers_list)

numbers_list.append(5)
print(numbers_list)

# add more than one element in a list
numbers_list.extend([6, 7])
print(numbers_list)

numbers_list.insert(0, 777)
print(numbers_list)

# remove last item in the list
numbers_list.pop()
print(numbers_list)

# remove item in index 1
numbers_list.pop(1)
print(numbers_list)

# remove 777
numbers_list.remove(777)
print(numbers_list)

# sort
numbers_list.sort()
print(numbers_list)

# return a sorted list
print(sorted(numbers_list))

# copy list
# ❌bad
a = [1, 2, 3, 22, 4, 0, 10]
b = a # bab practice

#  superficial
x = a.copy()
# o
x = a[::-1] # invertir el orden
x = a[0:2]
x = a[0:7:2]
# [ inicio : fin : paso ] paso: es el salto que da para tomar un elemento
# por ejemplo paso = 2, va de 2 en 2 tomando elementos en este caso.
# [1, 2, 3, 22, 4, 0, 10] => a[0:7:2] =>  1, 3, 4, 10

print(x)

# deep copy
y = copy.deepcopy(a)
y.append(777)
print(y)
print(a)

# matriz
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrizCopy = matriz.copy()

# modify matriz
matrizCopy.append([10, 11, 12])
# las listas son las que tienen referencia, la matriz no
print(matriz)

# modificar una lista
# matrizCopy[0].append(88)
# print(matriz)

# with deepcopy, it creates a new nested list
matrizCopy2 = copy.deepcopy(matriz)
matrizCopy2[0].append(777)
print(matrizCopy2)
print(matriz)

sum_value = 0
for item in numbers_list:
    sum_value += item

print(numbers_list)
print(sum_value)

list_exercise = [1, 2, -10, 3, 22, -8, 4, 0, 10, -2]

print(list_exercise)
for idx, item in enumerate(list_exercise):
    if item < 0:
        list_exercise.pop(idx)
        list_exercise.insert(idx, 0)

print(list_exercise)

# ▶️Implementa deep_clone(obj) sin usar deepcopy(). Debe soportar:
#
# listas
# diccionarios
# sets
# tuplas
# valores anidados





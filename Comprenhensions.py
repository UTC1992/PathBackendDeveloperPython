result = [x * 2 for x in range(10)]
print(result)

# list dentro de corchetes
result = [x * 2 for x in range(10) if x % 2 == 0]
print(result)

animals = ["Dog", "Cat", "Bird"]
# dictionary dentro de llaves
result = { f"name{i}": a for i, a in enumerate(animals, start=1) }
print(result)

result = [{ "name": a } for a in animals]
print(result)

# set o conjunto dentro de llaves { }
data = { x * x for x in [1,2,2,3] }
print(data)

# generator expression entre parentesis
data = (x * 2 for x in range(1000000000))
for i, value in enumerate(data):
    print(f"index {i}: value => {value}")
    if i == 5:
        break

# limpiar datos o crear una lista con datos que dependen de un valor en este caso si estan activos
users = [{"name": "juan", "isActive": False}, { "name": "joe", "isActive": True}]
active_users = [u for u in users if u["isActive"]]
print(active_users)

# create index for values in this case about name example: { juan: { data }, pedro: { data } }
users_indexed = {u["name"]: u for u in users}
print(users_indexed)

# flat matrices o aplanar matrices
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matriz)
matriz_flat = [x for row in matriz for x in row]
print(matriz_flat)

# count data when pass evaluation
users_with_age = [{"name": "juan", "isActive": False, "age": 21 }, { "name": "joe", "isActive": True, "age": 17}]
count = len([u for u in users_with_age if u["age"] >= 18])
print(count)
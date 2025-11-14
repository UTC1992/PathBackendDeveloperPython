person = {"name": "John", "age": 25}
print(person)

# get ( key, default_value )
age = person.get("age", 0)
print(age)

# object or nested dictionaries
data = {"user": {"name": "John", "age": 25, "book": {"title": "Python"}}}
print(data)

print(person.items())
print(person.keys())
print(person.values())


person = {"name": "John", "age": 25}
print(person)

# get ( key, default_value )
age = person.get("age", 0)
print(age)

# object or nested dictionaries
data = {"user": {"name": "John", "age": 25, "book": {"title": "Python"}}, "book": {"title": "Python"}}
print(data)

print(person.items())
print(person.keys())
print(person.values())

print(data)
demo = data.pop("demo", None) # if it is not in the dictionary return default value in this case None
book = data.pop("book", None) # remove a key - value and return value
name = data["user"].pop("name", None) # remove a key value nested and return value
print(name)
print(name)
print(data)

# data.popitem()
print(data)

def safe_get(dictionary, path):
    keys = path.split(".")
    new_dictionary = dictionary
    for key in keys:
        if not isinstance(new_dictionary, dict):
            return None
        if key not in new_dictionary:
            return None
        new_dictionary = new_dictionary[key]

    return new_dictionary

print(safe_get(data, "user.book.title"))

# set value by default if it is not exist
# or get value if it is present
car =  {"model": "Ford", "color": "black"}
print(car)
car.setdefault("year", 2000)
print(car.setdefault("model", None))
print(car)


example = {"a": {"b": {"c": 5}, "d": {"e": 6}}}
print(example)
print(example.keys())

def flatten_keys(dictionary: dict, prefix: str = "") -> dict:
    current_dic = dictionary
    new_dic = {}

    for key, value in current_dic.items():
        new_key = f"{prefix}{key}"

        if isinstance(value, dict):
            new_dic.update(flatten_keys(value, new_key + "."))
        else:
            new_dic.update({new_key: value})

    return new_dic


# return: {'a.b.c': 5, 'a.d.e': 6}
print(flatten_keys(example))



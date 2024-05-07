# Dictionary datatypes - similar to HashMap in Java, takes key-value pair

dict1 = {"name": "Allwyn", "age": 36, 2: True}

print(dict1["name"])  # print the value

dict1["nachtname"] = "Oommen"  # adding a new key-value pair

print(dict1.__contains__(2))  # contains value ?

print(dict1.__setitem__("Ort", "Boeblingen"))  # appends a new k-v pair

dict2 = {}

dict2.update({"vorname": "Sam baby", "geburtsjahre": 2024})


dict2["ort"]= "Stuttgart"
print(dict2)

del dict2["ort"]  # deletes an element from the Iterable based on key
print(dict2)

print("Keys -> {}".format(dict1.keys()))  # displays list of keys

print("Values -> {}".format(dict1.values()))  # displays all the list of values

print("Key-values -> {}".format(dict1.items()))  # displays list of key-val pairs

# print(dict1.pop())  # removes element by key and displays the removed value

print(dict2.popitem())

print(dict1)



# print

print("Hello World python!")

a, b = "Hello", 3000

# printing different datatype values together

print("{} world {}".format(a,b))

# Datatypes

x = 20  # number datatype - int, float and complex numbers
y = "Allwyn"  # String datatype

# list - mutable
ls = [1,2,"hello", 2.5,1,2,1,1]  #list - same as array in java

ls[2] = "HELLO"  # change the value of the list. Remember that list is mutable.

print(ls)

# list operations
ls.pop(2)  # removes a element based on the index

ls2 = ls.copy()  # copies the list to another list

ls2.sort()  # sorts in Asc order

ls.sort(reverse=True)  # sorts in Desc order

counts = ls.count(1)  # counts the occurrence of the element oin the list

ls.append(3000)

ls.remove(1)  # removes the first found value

ls.insert(2, "Samuel")  # inserts an element at an index

ls3 = [4,5,6]
ls.extend(ls3)  # extends list with another iterable such as list, set or tuple

val = ls.__contains__(4)  # checks if list contains an object

ls.__setitem__(2, "SetsItem")

ls3.clear()  # clears the list

occurrence = ls.index(3000)  # finds the first occurrence of the item, returns index

print("Occurrence > ", occurrence)

print("val: ", val)

print(ls)

# printing the range of values from the list
print("Range: ", ls[1:4])  # prints the range from 1-3, excluding 4
print("Counts: ", counts)



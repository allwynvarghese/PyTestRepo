# Tuple datatype - This is immutable
# note: Tuple is written in round brackets, whereas list is described in square brackets

tp = (1,3,"Hello",3)

val = tp.count(3)  # counts the value of elements in the tuple
print("Count is {}".format(val))

getIndex = tp.index("Hello")  # get index of the element in the tuple
print("Index of hello is ", getIndex)

status = tp.__contains__(3)  # check if tuple contains an element
print("Contains status > {}".format(tp.__contains__(3)))

count = tp.count(3)  # counts the number of elements in the tuple
print("Counts > {}".format(count))

print(tp)




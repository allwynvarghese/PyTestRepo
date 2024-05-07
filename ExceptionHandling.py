# raise key word is used to raise an exception

itemsInCart = 2

if itemsInCart < 1:
    raise Exception("Your cart cannot be empty")

# assert method in python check for assertion of conditions
itemsOrdered = 6

assert (itemsOrdered >= 5)

# try/except block to handle errors give custom message in except block
try:
    with open('filelog.txt', 'r') as log:
        print(log.readline())
except:
    print("!!!File not found!!!")  # printing custom error message

# try/except,finally block to handle errors giving python error message
try:
    with open('filelog.txt', 'r') as log:
        print(log.readline())
except Exception as e:
    print(e)
finally:  # finally comes after try or except block
    print("finally printing text")


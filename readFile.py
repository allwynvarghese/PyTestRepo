# open and read file

file = open('text.txt')  # opens a text file to read

print(file.read())  # reads all data from the file

print(file.read(5))  # reads 5 character from the file

print(file.readline())  # reads a single line from the file

#  readline method in while loop to read all lines from the file
line = file.readline()
while line != "":
    print(line)
    line = file.readline()

# readLines method stores all the lines in a list
for line in file.readlines():
    print(line)

file.close()  # close the file


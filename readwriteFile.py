# read the file and store all the lines in a list
# reverse the list
# Write back the reversed content in the file

with open('text.txt', 'r') as file:  # another way to read file. 'r' indicates read mode.
    # No need to close file here, it automatically closes once the loop is over
    content = file.readlines()
    with open('text.txt', 'w') as writer:  # open file in write mode
        for line in reversed(content):  # reversed method is used to reverse the list
            writer.write(line)  # write method is used to write into the file

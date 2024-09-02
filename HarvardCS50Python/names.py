#I/O In Python


# open a file, read it and sort and the print out all the line

names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

# sorted function can take parameters as well sorted(iterable, /, *, key=None, reverse=False)
for name in sorted(names, reverse=True):
    print(f"hello,  {name}")

# name = input("What's you name?")

# open('filename', 'w' for writing to the file)
# open returns a file assigned, in the example below file
# a is to append to an existing file

# with open will close file after the indented code block ends
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")


# explicitly opening file and calling close
# file = open("names.txt", "a")
# file.write(f"{name}\n")

# explicity close
# file.close()

# with open the second parameter "r" is for reading the file
# with open("names.txt", "r") as file:
#     for line in file:
#         print("hello", line.rstrip())


# with open("names.txt", "r") as file:
#     lines = file.readlines()

# for line in lines:
#     print("hello, ", line.rstrip())



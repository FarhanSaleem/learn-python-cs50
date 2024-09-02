# (to="world") sets the default value of parameter to

# def main():
#     name= input("What's your name? ")
#     hello(name)


# def hello(to="world"):
#     print("hello,", to)

def main():
    x = int(input("What's x? "))
    print("x squared is ", square(x))

def square(n):
    return n * n

main()
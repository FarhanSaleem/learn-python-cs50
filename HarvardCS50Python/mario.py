def main():
    print_square(3)


def print_column(height):
    # for _ in range(height): 
    # print("$")
    # OR
    print("#\n" * height, end="")

        

def print_row(width):
    print("#" * width)

def print_square(number):
    for _ in range(number):
     print_row(number)


main()
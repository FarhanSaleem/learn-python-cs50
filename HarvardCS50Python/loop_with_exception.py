# create a function that gets called in a loop until condition is met
# throwing an exception when the user input is not in correct format

def main():
    x = get_init("What's x? ")
    print(f"x is {x}")

def get_init(prompt):
    while True:
        try:
            # if the input is correct format, break the loop and return th value
            return int(input(prompt))
        except ValueError:
            print("x is not a number")
            
          
    

main()


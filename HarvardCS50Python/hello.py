# #Ask user for their name and chain functions 

# name = input("What's your name? ").strip().title()

# # Remove whitespace from string & captalize user's name
# # name = name.strip().title()

# # Split user's name into first name and last name
# first, last = name.split(" ")

# print(f"hello, {first} :)", end="")

def main():
    name = input("What's your name?")
    print(hello(name))

def hello(to="world"):
    return f"hello, {to}"

if __name__ == "__main__":
    main()
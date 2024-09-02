import array as A
# for loops
# arr = A.array('i', [0, 1, 2])
# arrlength = len(arr)

# for _ in range(arrlength):
#     print("meow")

# iterate with print by giving it a mulitplier
# n = int(input("What's n? "))
# print("meow\n" * 3, end="")


# #while example
# i = 0
# while i < 4:
#     print("meow")
#     i += 2

# ask user a question and until the answer is satisfactory 
# stay in loop infinitely with while True, once condition is match proceed
while True:
    n = int(input("What's n?"))
    if n > 0:
        break

for _ in range(n):
    print("meow")
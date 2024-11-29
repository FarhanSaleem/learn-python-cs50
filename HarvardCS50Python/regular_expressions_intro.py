import re

email = input("what's your email? ")

if re.search(".+@.+", email):
    print("Valid")
else:
    print("Invalid")
# import python csv module to help read , write to csv files with built in functions
import csv

# read comma delimited csv file

ppl = []

with open("csv_read.csv") as file:
    # csv.reader creates a reader which you can use as a list of columns
    #reader = csv.reader(file)

    # csv.DictReader returns a dictionary reader which you can access the key of any object in that dictionary
    reader = csv.DictReader(file)
    for row in reader:
        ppl.append({"name": row["name"], "city": row["city"]})

# custom csv reading code we wrote
# with open("commadelimiteddata.csv") as file:
#     for line in file:
#         name, city = line.rstrip().split(",")
#         person = { "name": name, "city": city }
#         ppl.append(person) 

def get_name(person):
    return person["name"]

# to give the sorted key an explicit function to sort by, the function returns the key to the sorted function
# for person in sorted(ppl, key=get_name, reverse=True):

# call lambda function if its only called once, followed by parameter the function will take, then : name of key in person that you want to return
for person in sorted(ppl, key=lambda person: person["name"]):
    print(f"{person['name']} is in {person['city']}")
      


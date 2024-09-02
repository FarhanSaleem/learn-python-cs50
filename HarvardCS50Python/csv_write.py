import csv

name = input("what is this person's name? ")
city = input("In what city do they live? ")

with open("csv_write.csv", "a") as file:
    # writer = csv.writer(file)
    # writer.writerow([name, city])
    writer = csv.DictWriter(file, fieldnames=["name", "city"])
    writer.writerow({"name": name, "city": city})
   
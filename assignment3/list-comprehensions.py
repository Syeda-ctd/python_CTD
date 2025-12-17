import csv

#1 read employees.csv into a list of lists
with open("../csv/employees.csv", "r") as file:
    reader = csv.reader(file)
    rows = list(reader)    

#create a list of full employee names (skip header)
employees_names = [row[1] + " " + row[2] for row in rows[1:]]

print("All employee names: ")
print(employees_names)

#create another list with e names
names_with_e = [name for name in employees_names if "e" in name.lower()]

print("\nNames containing the letter 'e':")
print(names_with_e)


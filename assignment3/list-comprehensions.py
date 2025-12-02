import csv

# ---------- Read CSV into a list of lists ----------
employees_file = "../csv/employees.csv"

with open(employees_file, newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    employee_data = list(reader)  # list of lists

# ----------  List of full names (skip header) ----------
# full name = first_name + " " + last_name
full_names = [f"{row[0]} {row[1]}" for row in employee_data[1:]]  # skip header row
print("All employee names:")
print(full_names)

# ----------  Names containing the letter "e" ----------
names_with_e = [name for name in full_names if "e" in name.lower()]  # case-insensitive
print("\nEmployee names containing 'e':")
print(names_with_e)
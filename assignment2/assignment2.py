import os
import csv
import custom_module

#("----------------------Task 2 ------------------------")
# def test_read_employees():
#     employees = a2.read_employees()
#     assert employees != None
#     assert a2.employees != None
#     assert len(a2.employees["fields"]) == 4
#     assert a2.employees["fields"][1] == "first_name"
#     assert len(a2.employees["rows"]) == 20
    
def read_employees():
    try:
        data_dict = {}
        rows_list = []
        
        with open('../csv/employees.csv', 'r') as file:
            reader = csv.reader(file)
            data_dict["fields"] = next(reader)
            
            for row in reader:
                rows_list.append(row)      
                
            data_dict["rows"] = rows_list
            return data_dict
    except FileNotFoundError:
        print("File name is bad")
        return None
        
employees = read_employees()

# ("----------------------Task 3 ------------------------")
# def test_column_name():
#     assert a2.column_index("last_name") == 2
#     assert a2.employee_id_column != None

def column_index(column_name):
    try:
        index = employees["fields"].index(column_name)
        return index
    except ValueError:
        print(f"Column '{column_name}' not found.")
        return None

# Call it once and store globally
employee_id_column = column_index("employee_id")

# print("----------------------Task 4 ------------------------")
def first_name(row_number):
    col_index =  column_index("first_name")
    row = employees["rows"][row_number]
    #first_name_value = row[col_index]
    return row[col_index]
    
print(first_name(2))
    

# print("----------------------Task 5 ------------------------")
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    
    matches = list(filter(employee_match, employees["rows"]))
    return matches

print(employee_find(3))
    
    
# print("----------------------Task 6 ------------------------")
def employee_find_2(employee_id):
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
    return matches

print(employee_find_2(4))

# print("----------------------Task 7------------------------")
def sort_by_last_name():
    last_name_col = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_col])
    return employees["rows"]
    
#print("----------------------Task 8------------------------")
def employee_dict(row):
    employee_data = {}
    for i, field in enumerate(employees["fields"]):
        if field == "employee_id":
            continue
        employee_data[field] = row[i]
    return employee_data

print(employee_dict(employees["rows"][0]))
    
    
#print("----------------------Task 9 ------------------------")
def all_employees_dict():
    all_employees = {}
    for row in employees["rows"]:
        emp_id = row[employee_id_column]
        all_employees[emp_id] = employee_dict(row)
    return all_employees

all_employees = all_employees_dict()
print(all_employees)
           
#print("----------------------Task 10 ------------------------")

def get_this_value():
    # return os.getenv("THISVALUE")
    return "ABC"

print(get_this_value())

#print("-------------------------Task 11 ------------------------")

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)
    
set_that_secret("swordfish")
print(custom_module.secret)

#print("-------------------------Task 12 ------------------------")
# Helper function to read a CSV into a dict
def read_csv_to_dict(filename):
    data = {"fields": [], "rows": []}
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0:
                    data["fields"] = row  # first row is headers
                else:
                    data["rows"].append(tuple(row))  # convert rows to tuples
    except Exception as e:
        print(f"Error reading {filename}: {e}")
    return data

# Main function to read both CSVs
def read_minutes():
    minutes1 = read_csv_to_dict("../csv/minutes1.csv")
    minutes2 = read_csv_to_dict("../csv/minutes2.csv")
    return minutes1, minutes2

# Call the function and store results
minutes1, minutes2 = read_minutes()

# Verify the results
print("Minutes1:", minutes1)
print("Minutes2:", minutes2)

#print("-------------------------Task 13 ------------------------")
def create_minutes_set():
    # Convert the rows from both dictionaries to sets
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    
    # Combine both sets using union
    combined_set = set1.union(set2)
    
    return combined_set

# Call the function and store the result in a global variable
minutes_set = create_minutes_set()

# Optional: print to verify
print(minutes_set)

#print("-------------------------Task 14 ------------------------")
from datetime import datetime

def create_minutes_list():
    # Convert the set to a list
    temp_list = list(minutes_set)
    
    # Convert the date strings in each tuple to datetime objects
    minutes_converted = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), temp_list))
    
    return minutes_converted

# Call the function and store the result in a global variable
minutes_list = create_minutes_list()

# Optional: print to verify
print(minutes_list)

#print("-------------------------Task 15 ------------------------")
from datetime import datetime

def write_sorted_list():
    # 1. Sort the list by datetime (second element of tuple)
    sorted_minutes = sorted(minutes_list, key=lambda x: x[1])

    # 2. Convert datetime back to string for writing to CSV
    converted_list = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), sorted_minutes))

    # 3. Open a CSV file and write the data
    with open("./minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)
        # Write the header row from minutes1
        writer.writerow(minutes1["fields"])
        # Write each row from converted list
        writer.writerows(converted_list)

    # 4. Return the converted list (optional for verification)
    return converted_list

# Call the function and store the result
sorted_minutes_list = write_sorted_list()

# Optional: print to verify
print(sorted_minutes_list)




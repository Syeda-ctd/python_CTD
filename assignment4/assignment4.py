#---------------------------------Task 1: Introduction to Pandas - Creating and Manipulating DataFrames---------
import pandas as pd
import numpy as np
import json

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
task1_data_frame = pd.DataFrame(data)
print("Original DataFrame:")
print(task1_data_frame)

task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
print("\nDataFrame with Salary:")
print(task1_with_salary)

task1_older = task1_with_salary.copy()
task1_older['Age'] = task1_older['Age'] + 1
print("\nDataFrame with Incremented Age:")
print(task1_older)

task1_older.to_csv('employees.csv', index=False)
print("\nData saved to employees.csv")

#-------------------------Task 2: Loading Data from CSV and JSON--------------------------


# Load the data from a CSV file
task2_employees = pd.read_csv('employees.csv')
print(task2_employees)

# Load the data from a JSON file
#create a JSON data
additional_employees_json = [
    {'Name':'Eve', 'Age':28, 'City': 'Miami', 'Salary':60000},
    {'Name':'Frank', 'Age':40, 'City': 'Seattle', 'Salary':95000}
]

with open('additional_employees.json', 'w') as f:               #save the list as JSON file
    json.dump(additional_employees_json, f, indent=4)

json_employees = pd.read_json('additional_employees.json')   #Read the JSON file into a DataFrame
print(json_employees)

more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print(more_employees)


#-------------------------Task 3:  Data Inspection - Using Head, Tail, and Info Methods--------------------------
# Use the head() method:
# Assign the first three rows of the more_employees DataFrame to the variable first_three
# Print the variable and run the tests.

first_three = more_employees.head(3)
print(first_three)

# Use the tail() method:
# Assign the last two rows of the more_employees DataFrame to the variable last_two
# Print the variable and run the tests.
last_two = more_employees.tail(2)
print(last_two)

# Get the shape of a DataFrame
# Assign the shape of the more_employees DataFrame to the variable employee_shape
# Print the variable and run the tests
employee_shape = more_employees.shape
print(employee_shape)

more_employees.info()

#----------------- Task 4: Data Cleaning ------------------------------

# Step 1: Read the dirty data
dirty_data = pd.read_csv('dirty_data.csv')
print("Original dirty data:")
print(dirty_data)

# Step 2: Create a copy for cleaning
clean_data = dirty_data.copy()

# Step 3: Remove duplicate rows
clean_data.drop_duplicates(inplace=True)
print("\nAfter removing duplicates:")
print(clean_data)

# Step 4: Convert Age to numeric (force non-numeric to NaN)
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')
print("\nAfter converting Age to numeric:")
print(clean_data)

# Step 5: Convert Salary to numeric (replace placeholders like 'unknown' or 'n/a' with NaN)
clean_data['Salary'] = clean_data['Salary'].replace(['unknown', 'n/a'], np.nan)
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')
print("\nAfter converting Salary to numeric:")
print(clean_data)

# Step 6: Fill missing values (Age → mean, Salary → median)
clean_data['Age'].fillna(clean_data['Age'].mean(), inplace=True)
clean_data['Salary'].fillna(clean_data['Salary'].median(), inplace=True)
print("\nAfter filling missing values:")
print(clean_data)

# Step 7: Convert Hire Date to datetime
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], errors='coerce')
print("\nAfter converting Hire Date to datetime:")
print(clean_data)

# Step 8: Strip whitespace and standardize Name & Department to uppercase
clean_data['Name'] = clean_data['Name'].str.strip().str.upper()
clean_data['Department'] = clean_data['Department'].str.strip().str.upper()
print("\nAfter cleaning text fields:")
print(clean_data)




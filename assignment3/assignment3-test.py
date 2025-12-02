import assignment3 as a3
import numpy as np
import pandas as pd
import os

test1_df = pd.DataFrame({   'Name': ['Alice', 'Bob', 'charlie'], 
                            'Age': [25, 30, 35], 
                            'City': ['New York', 'Los Angeles', 'Chicago']})

def test_data_frame_from_dictionary():
    assert test1_df.equals(a3.task1_data_frame)

def test_added_column():
    assert a3.task1_with_salary['Salary'].equals(pd.Series([70000, 80000, 90000]))

def test_increment_column():
    assert a3.task1_older["Age"].equals(pd.Series([26, 31, 36]))

def test_write_csv():
    assert os.access("./employees.csv", os.F_OK) == True



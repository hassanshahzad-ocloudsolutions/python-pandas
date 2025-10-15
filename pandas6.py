
import pandas as pd
import numpy as np 
from faker import Faker

'''
Addition/Removal of data in data frame this can be row as well as coloumn
'''

def addition_removal():
    #adding a new coloumn with default values in data frame only in RAM
    data = pd.read_excel("./student_records.xlsx")
    data['Campus'] = 'OC' #BY DEFAULT OC
    print(data.head())
    print("\n")

    #putting 101 to 150 students in OC and 151 to 200 in NC

    #where is used for conditioning
    data['Campus'] = np.where(data['Student ID']<=150, 'OC', 'NC')
    print(data.head())
    print(data.tail())
    print("\n")

    #storing in a variable as data.drop() returns a new data frame
    data_frame_with_removed_campus = data.drop(columns=['Campus'])
    print(data_frame_with_removed_campus.head())

    #renaming the headings
    rename_data = data.rename(columns={'Student ID': 'ID', 'Name':'Full Name', 'GPA':'CGPA'})
    print(rename_data)

def copy_data_frame():
    student = pd.read_excel("./student_records.xlsx")
    new_student = student.copy() #deep copy, both pointing to separate memory locations
    print(id(new_student)==id(student))

    fake = Faker()
    new_student['DOB'] = [fake.date_of_birth(minimum_age=18, maximum_age=25) for i in range(new_student.shape[0])]
    print("Student Data with DOBs")
    print(new_student)
    print("\n")

    #using date_time object
    print("First 10 Students with Highest GPA and Birth Year ")
    new_student['DOB2'] = pd.to_datetime(new_student['DOB'])
    new_student['Birth Year'] = new_student['DOB2'].dt.year
    print(new_student[['Name', 'GPA','DOB', 'Birth Year']])



#addition_removal()
copy_data_frame()
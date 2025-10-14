import pandas as pd
'''
Accessing data using pandas

Both allows us to filter on basis of rows and coloumns

loc -> selects data by labels (names).
iloc -> selects data by positions (indexes).
'''

def function_loc():
    students = pd.read_excel("./student_records.xlsx")
    print("All Records")
    print(students.loc[:])
    print("\n")

    print("Selected Rows And Coloums")
    s1 = students.loc[0,'Student ID']
    print(s1)
    print(type(s1)) # numpy int
    print("\n")

    s2 = students.loc[[0,1,2,3,4,5,6], 'Student ID']
    print(s2)
    print(type(s2)) # Pandas Series (1D)
    print("\n")

    s3 = students.loc[[0,1,2,3,4,5,6], ['Student ID', 'Age']]
    print(s3)
    print(type(s3)) # Pandas Data Frame (1D)
    print("\n")

    s4 = students.loc[0:10, ['Student ID', 'Age']] # 0 to 10 inclusive only two coloumns
    print(s4)
    print(type(s4)) # Pandas Data Frame (1D)
    print("\n")

def function_iloc():
    students = pd.read_excel("./student_records.xlsx")

    s1 = students.iloc[0,0]
    print(s1)
    print("\n")

    s2 = students.iloc[0, 1:3]
    print(s2)
    print("\n")

    s3 = students.iloc[0:10, 1:3] # 0 to 9 and 1 to 2 as here we are specifying to index not the attributes
    print(s3)
    print("\n")

    s4 = students.iloc[[0,1,2,3,4], [0,1,2,3,4]] # All indexes inclusive
    print(s4)
    print("\n")


function_loc()
function_iloc()

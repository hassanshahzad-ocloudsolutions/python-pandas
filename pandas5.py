import pandas as pd

'''
Filtering data using pandas, only retrieve data that meets over specific conditions
'''

def filtering_data():
    data = pd.read_excel("./student_records.xlsx")

    print("Students with GPA greater than 3")
    print(data.loc[data['GPA']>3])
    print("\n")

    print("Students with GPA greater than 3 and Sorted")
    print((data.loc[data['GPA']>3]).sort_values('GPA' , ascending=True))
    print("\n")

    print("Students with age between 18 and 20")
    print(data.loc[((data['Age']>=18) & (data['Age']<=20)), ['Name','Age']])
    print("\n")

    print("Names starting with A")
    print(data.loc[data['Name'].str.startswith("A"), ['Student ID','Name']])
    print("\n")

    print("Names containing A or B or S")
    print(data.loc[data['Name'].str.contains("A|B| S"), ['Student ID','Name']])
    print("\n")

#use for clarity
def query_function():
    data = pd.read_excel("./student_records.xlsx")

    print("Students with age between 18 and 20")
    print(data.query('Age>=18 & Age<=20'))
    print("\n")

    print("Students with age between 18 and 20 sorted")
    print(data.query('Age >= 18 & Age <= 20').sort_values('Name', ascending=True))


filtering_data()
query_function()
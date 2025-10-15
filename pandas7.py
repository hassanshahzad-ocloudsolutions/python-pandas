import pandas as pd

#Applying lambda functions on our data frame

students = pd.read_excel("./student_records.xlsx")
grades = pd.read_excel("./student_grades.xlsx")
def custom_columns():
    students['Campus'] =  students['Student ID'].apply(lambda x: 'OC' if x<=150 else 'NC')
    print(students)
    print("\n")

#like join in sql
def merging():
    #both below statements give same results 
    #left_on specifies the coloumn to be taken from left table and right_on specifies the coloumn to be taken from right table
    #how (left, right,inner) same as inner and outer join
    merged1 = pd.merge(students, grades, on='Student ID', how='inner')
    merged2 = pd.merge(students, grades ,left_on='Student ID', right_on='Student ID', how='inner')
    print(merged1.head())
    print(merged2.head())

def concatenating():
    lesser_than_3_GPA = students[students['GPA']<3]
    greater_than_3_GPA = students[students['GPA']>=3]
    concatenated_df = pd.concat([lesser_than_3_GPA, greater_than_3_GPA]).sort_values('GPA', ascending=True)
    print(concatenated_df)


custom_columns()
merging()
concatenating()
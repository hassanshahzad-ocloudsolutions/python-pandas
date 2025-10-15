'''
Aggregation

Aggregating data in Pandas means summarizing or combining multiple rows of data into
meaningful statistics (like sum, mean, count, etc.), often grouped by one or more columns.
'''
import pandas as pd
import numpy as np

students = pd.read_excel("./student_records.xlsx")

def aggregating_data_function():
    #Counting occurence of students with respect to their GPA
    print(students['GPA'].value_counts())

    #Counting occurences of students with respect to their age
    print(students['Age'].value_counts)

    #Counting Occurences of students with respect to their names
    print(students['Name'].value_counts())

    #Value count using filter
    print(students[students['Name']=='Bilal']['Name'].value_counts())

    #Counting Bilal name students with respect to their age
    print(students[students['Name']=='Bilal']['Age'].value_counts())

def group_by():
    # grouping data on name basis
    group1 = students.groupby(['Name']).size()
    print(group1)

    #taking average of ages based on names
    group2 = students.groupby(['Name'])['Age'].mean()
    print(group2)

    #Multiple operations
    group3 = students.groupby(['Department']).agg({'Age': 'mean', 'GPA':'max'})
    print(group3)
    '''
    Output seems like this

                      Age   GPA
Department                 
AI          21.500000  3.14
BBA         21.875000  3.94
CS          22.071429  3.98
Cyber       21.444444  3.91
DS          22.000000  3.87
EE          22.764706  3.99
IT          21.333333  3.90
SE          21.235294  3.79
    '''

    #Can group on multiple attributes basis
    group4 = students.groupby(['Department', 'Name']).agg({'Age': 'mean', 'GPA':'max'})
    print(group4)

aggregating_functions()
group_by()
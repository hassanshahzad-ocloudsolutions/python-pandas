
import pandas as pd
students = pd.read_excel("./student_records.xlsx")

#pivot in pandas
'''
pivot() reshapes the data ie row into coloumns and coloumns into rows
'''
def pivot_example():
    print(students.head())
    print("\n")

    #removing duplicates so we can easily reshapes else we will encounter error due to duplication of data
    new_students = students.drop_duplicates(subset=['Name', 'GPA'])
    pivot_data = new_students.pivot(columns = 'Name', index='GPA', values='Age')
    print(pivot_data.head())
    print("\n")

'''
shift(), rank(), rolling()
'''
def advance_functionality():

    print("Illustrating shift() function")
    students['prev_GPA'] = students['GPA'].shift(1)
    print(students)
    print("\n")

    # we can also get floating point ranks this happens when there are two or more rows with same value then their average is assigned as a rank
    print("Illustrating rank() function")
    students['GPA_rank'] = students['GPA'].rank(ascending=False) #highest GPA = Rank1 and vice versa if ascending = False not set than by default it would be lowest GPA = Rank1
    print(students)
    print("\n")

    print("Illustrating rolling() function")
    students['Rolling_avg_GPA'] = students['GPA'].rolling(window=3).mean()
    print(students.head(6))
    print("\n")

pivot_example()
advance_functionality()

import pandas as pd

'''
at -> gives only single cell based on the row and coloumn name
iat -> gives only single cell based on the indexes
'''

def at_iat():
    data = pd.read_csv('./lung_cancer_examples.csv')
    print(data.at[0,'Name'])
    print(data.iat[0,0])

def other_ways_to_access_data():
    data = pd.read_excel('./student_records.xlsx')
    print(data['Student ID'])
    print(data[['Student ID', 'Age']])
    print(data.Age) #works only for coloumns without spaces
    # print(data [0, ['Student ID','Age']]) will give error as it takes only on parameter ie coloumns
    print(data.sort_values("Age")) # sorts data on age basis
    print(data.sort_values("Age")[0:10])
    print(data.sort_values(['Name','Age'])) #sorting on basis of two parameters, first sort on 1st pararmeter basis then on second parameter basis
    print((data.sort_values("Name", ascending=False)).loc[[0,1,2,3], ['Student ID', 'Name']])
    print((data.sort_values("Name", ascending=False)).loc[0:10, ['Student ID', 'Name']])
    print(data.sort_values(['Name','GPA'], ascending=[False, True])) #first parameter descending, second parameter ascending

def looping_data():
    data = pd.read_excel('./student_records.xlsx')

    #not recommended
    for index, row in data.iterrows():
        print(index)
        print(row)
        print("\n")
    

at_iat()
other_ways_to_access_data()
looping_data()
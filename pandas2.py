import pandas as pd 
import sys
'''
Loading data from files into data frames
'''

def csv():
    csv_data = pd.read_csv("./lung_cancer_examples.csv")
    print(csv_data.info())
    print(csv_data.describe())
    print(csv_data.columns.to_list())
    print(csv_data.index.to_list())
    print(csv_data.sample(10)) #10 random records
    print(csv_data.head(10))
    print(csv_data.tail(10))

def excel():
    excel_data = pd.read_excel("./student_records.xlsx")
    print(excel_data.info())
    print(excel_data.describe())
    print(excel_data.columns.to_list())
    print(excel_data.index.to_list())
    print(excel_data.sample(10)) #10 random records
    print(excel_data.head(10))
    print(excel_data.tail(10))


csv()
excel()




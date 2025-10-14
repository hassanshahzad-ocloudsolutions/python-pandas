
'''
pandas is a useful tool that helps in data ingestion(loding data from csv, exce, db) into RAM,
data visualization(with help of matplotlib, seaborn), data analysis, data manipulation, time series functionalities.
'''

import pandas as pd 

'''
dataframe, a tabular structure use to store data retrieved from csv, excel file
'''
data_frame1 = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])
print("Data Frame 1")
print(data_frame1)   

print("\n")

data_frame2 = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9],[1,2,3],[4,5,6],[7,8,9]],columns=["col1","col2","col3"],index=["row1","row2","row3","row4","row5","row6"])
print("Data Frame 2")
print(data_frame2)

print("\n")

print("Data Frame 2 Head")
print(data_frame2.head()) # default is first 5 rows

print("\n")

print("Data Frame 2 with First 2 Rows")
print(data_frame2.head(2))

print("\n")

print("Data Frame 2 Tail")
print(data_frame2.tail()) # default is last 5 rows

print("\n")

print("Data Frame 2 with Last 2 Rows")
print(data_frame2.tail(2))

print("\n")

print("Data Frame 2 Headings")
print(data_frame2.columns)

print("\n")

print("Data Frame 2 Headings")
for heading in data_frame2.columns:
    print(heading)

print("\n")

print("Data Frame 2 Index")
print(data_frame2.index)

print("\n")

print("Data Frame 2 Index")
for index in data_frame2.index:
    print(index)

print("\n")

print("Data Frame 2 Information")
print(data_frame2.info())

print("\n")

print("More Details About Data Frame 2s Coloumns")
print(data_frame2.describe())

print("\n")

print("Unique Values in Data Frame 2 Coloumns")
print(data_frame2.nunique()) #number unique

print("\n")

print("Unique Values in Data Frame 2 Coloumn 1")
print(data_frame2['col1'].unique()) #number unique

print("\n")

print("Shape of Data Frame 2")
print(data_frame2.shape) #number unique
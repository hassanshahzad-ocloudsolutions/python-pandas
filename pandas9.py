#Group By Example using pandas groupby

'''
input_list = [
    {"country": "Pakistan", "city": "Lahore", "state": "Punjab"},
    {"country": "Pakistan", "city": "Karachi", "state": "Sindh"},
    {"country": "Pakistan", "city": "Peshawar", "state": "KPK"},
    {"country": "Pakistan", "city": "Okara", "state": "Punjab"},
    {"country": "India", "city": "Delhi", "state": "Delhi"},
    {"country": "India", "city": "Mumbai", "state": "Maharashtra"},
    {"country": "India", "city": "Kolkata", "state": "West Bengal"},
    {"country": "USA", "city": "New York", "state": "New York"},
    {"country": "UK", "city": "Manchester", "state": "England"},
    {"country": "UK", "city": "London", "state": "England"}
]

output = 
{
    "Pakistan": [
        {"city": "Lahore", "state": "Punjab"},
        {"city": "Karachi", "state": "Sindh"},
        {"city": "Peshawar", "state": "KPK"},
        {"city": "Okara", "state": "Punjab"},
    ],
    "India": [
        {"city": "Delhi", "state": "Delhi"},
        {"city": "Mumbai", "state": "Maharashtra"},
        {"city": "Kolkata", "state": "West Bengal"},
    ],
    "USA": [{"city": "New York", "state": "New York"}],
    "UK": [
        {"city": "Manchester", "state": "England"},
        {"city": "London", "state": "England"},
    ],
}
'''

import pandas as pd

def group_by(li, by):
    data = pd.DataFrame(li)
    group_dict = {country:list((group[['city','state']]).to_dict(orient ='records'))
    for country, group in data.groupby(by)}
    return group_dict
    
    


input_list = [
    {"country": "Pakistan", "city": "Lahore", "state": "Punjab"},
    {"country": "Pakistan", "city": "Karachi", "state": "Sindh"},
    {"country": "Pakistan", "city": "Peshawar", "state": "KPK"},
    {"country": "Pakistan", "city": "Okara", "state": "Punjab"},
    {"country": "India", "city": "Delhi", "state": "Delhi"},
    {"country": "India", "city": "Mumbai", "state": "Maharashtra"},
    {"country": "India", "city": "Kolkata", "state": "West Bengal"},
    {"country": "USA", "city": "New York", "state": "New York"},
    {"country": "UK", "city": "Manchester", "state": "England"},
    {"country": "UK", "city": "London", "state": "England"}
] 

print(group_by(input_list, by='country'))
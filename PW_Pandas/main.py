
import pandas as pd
s=pd.read_csv('services.csv')
print(s)
s1=pd.read_csv('services.csv',header=None)#When we give header is None it vll give indexes as numbers for rows and columns
print(s1)
print(type(s1))
print(type(s))
print(list(s.columns))
print(s.head(5))
print(s.tail(5))
print(s.dtypes)
print(list(s["location_id"]))
print(s["audience"])
print(type(s["audience"]))#it v ll give u indexes becoz it is a series object 
print(list(s["audience"]))#it v ll not show u indexes becoz it is a list object 
print(type(s["location_id"]))
print(s[columns])


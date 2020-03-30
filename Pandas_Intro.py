# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 10:51:34 2020

@author: shubh
"""

#flexibility offered by python for pandas
#working with Big Data

#loading data into pandas from a csv file
import pandas as pd
dataFrame = pd.read_csv('pokemon_data.csv')
print(dataFrame)

#loading data into pandas from an excel file
df_xlx = pd.read_excel('pokemon_data.xlsx')

#see only the top three rows
print(dataFrame.head(3))
#see only the bottom three rows
print(dataFrame.tail(3))

#printing xslx data
print(df_xlx.head(100))

#reading a tab separated file as a csv without mentioning the delimiter
df = pd.read_csv('pokemon_data.txt')
print(df)
#now with specifying the delimiter
df = pd.read_csv('pokemon_data.txt',delimiter='\t')
print(df)


#reading just the headers in file
print(df.columns)
#printing data in a specific column
print(df['Name'][0:10]) #top 10 names
print(df.Name)

#if we want multiple columns at the same time, change it to a list
print(df[['Name','Defense','Attack']][0:10])
#read a particulra row
print(df.iloc[3])
#read a multiple of rows
print(df.iloc[3:6])
#read a specific location
print(df.iloc[3,2])

#using iterrows to iterate over index and the rows
for index, row in df.iterrows():
    print(row.Name)
#using next to see the contents of the iterator and printing the first item values
print(next(df.iterrows())[1])

#filtering based on a particular column value
print(df.loc[df['Type 1']=='Grass'].iloc[0:5,1:3])

#sort based on a column
print(df.sort_values('Name').iloc[:5,:2])
#no of unique value, value count
xrr =df['Type 1'].value_counts()
print(xrr)

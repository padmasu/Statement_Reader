'''This code will read through statements and will essentially output condensed versions'''
import pandas as pd
import time
import numpy as np
import csv


df = pd.read_csv(r"C:\Users\Phillipos Admasu\Documents\Statements\CSV\withdrawals.csv")
df = pd.DataFrame(df).set_index('UID')
#print(df)
df['Date'] = pd.to_datetime(df['Date'])

df['Day'] = df['Date'].dt.day_name()

#The following converts the Amount column to Float type. Replacing comma to complete conversion. 
df["Amount"] = df["Amount"].str.replace(',', '').astype(float)

#The following line displays the most common day transactions were made.
#It doesn't take into account the time transactions were made (Saturday night purchases technically are Sunday)
cd = df['Day'].mode()[0]
# print('-'*40)
# print("The most common day purchases were made is {}.\n".format(cd))
# print('-'*40)

# #The following displays the total number of transactions for each day.
# dailyc= df.Day.value_counts()
# print("\nTotal number of transactions for each day. (6 Month Period):\n{}".format(dailyc))
# print('-'*40)

# #The following displays the total amount spent for each day.
# amount_sum = df.groupby('Day').Amount.sum()
# print('\nTotal Amount spent for each day:\n{}'.format(amount_sum))
# print('-'*40)

# #The following will display which items were most costly/common.
# totali = df.Item.value_counts()
# print('\nThe most common item(s) purchased are:\n', totali)

#The following will combine items which are unnecessarily split. 
df2 = df[['Item', 'Amount']]
df2['Item'] = df2['Item'].to_string()
df2['Item'] = df2['Item'].str.lower()
df2['Item_type'] = pd.Series(dtype=str)

useri = input().lower()
test = df2.loc[df2['Item'].str.contains(useri)]

print(test)

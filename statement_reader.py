'''This code will read through statements and will essentially output condensed versions'''
import pandas as pd
import time
import numpy as np
import csv


df = pd.read_csv(r"C:\Users\Phillipos Admasu\Documents\Statements\CSV\withdrawals.csv")
df = pd.DataFrame()
print(df)
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
df2 = pd.DataFrame.append(df[['Item', 'Amount']])
df2 = df2.append(df, ignore_index = True)
df2['Item_type'] = pd.Series(dtype=str)


# test = df2.loc[df2['Item'].str.contains('McDonalds')]



# print(test)

item=['McDonalds Denver', 'Sonoco', 'ATM Fee', 'Sonoco, Ft. Collins', 'McDonalds, Boulder', 'Arco Boulder']
txn = [12.44, 4.00, 3.00, 14.99, 19.10, 52.99]
#df = pd.DataFrame([item, txn]).T

print(df2)


# let's add an extra column to catch the conversions...
#This will be df2['Item_type']***#df['item'] = pd.Series(dtype=str)

# we'll use the "contains" function in pandas as a simple converter...  quick demo
temp = df2.loc[df2['Item'].str.contains("McDonalds")]
# print('\nitems that contain the string "McDonalds"')
# print(temp)

# let's build a simple conversion table in a dictionary
conversions = { 'McDonalds': 'McDonalds - any',
                'Sonoco': 'gas',
                'Arco': 'gas'}

# let's loop over the orig items and put conversions into the new column
# (there is probably a faster way to do this, but for data with < 100K rows, who cares.)
# for key in conversions:
#     df2['item'].loc[df2['item_orig'].str.contains(key)] = conversions[key]

# # see how we did...
# print('converted...')
# print(df)

# # now move over anything that was NOT converted
# # in this example, this is just the ATM Fee item...
# df['item'].loc[df['item'].isnull()] = df['item_orig']


# # now we have decent labels to support grouping!
# print('\n\n  *** sum of charges by group ***')
# print(df.groupby('item')['charge'].sum())
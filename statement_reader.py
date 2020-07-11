'''This code will read through statements and will essentially output condensed versions'''
import pandas as pd
import time
import numpy as np
import csv


df = pd.read_csv(r"C:\Users\Phillipos Admasu\Documents\Statements\CSV\withdrawals.csv")
df = pd.DataFrame(df)

df['Date'] = pd.to_datetime(df['Date'])

df['Day'] = df['Date'].dt.day_name()

#The following converts the Amount column to Float type. Replacing comma to complete conversion. 
df["Amount"] = df["Amount"].str.replace(',', '').astype(float)

#The following line displays the most common day transactions were made.
#It doesn't take into account the time transactions were made (Saturday night purchases technically are Sunday)
cd = df['Day'].mode()[0]
print('-'*40)
print("The most common day purchases were made is {}.\n".format(cd))
print('-'*40)

#The following displays the total number of transactions for each day.
dailyc= df.Day.value_counts()
print("\nTotal number of transactions for each day. (6 Month Period):\n{}".format(dailyc))
print('-'*40)

#The following displays the total amount spent for each day.
amount_sum = df.groupby('Day').Amount.sum()
print('\nTotal Amount spent for each day:\n{}'.format(amount_sum))




# def main():
#     while True:
     
#      values(df)
 
# if __name__ == "__main__":
# 	main()
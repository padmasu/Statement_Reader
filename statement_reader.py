'''This code will read through statements and will essentially output condensed versions'''
import pandas as pd
import time
import numpy as np
import csv


df = pd.read_csv(r"C:\Users\Phillipos Admasu\Documents\Statements\CSV\withdrawals.csv")
df = pd.DataFrame(df)

df['Date'] = pd.to_datetime(df['Date'])

df['Day'] = df['Date'].dt.day_name()

#The following line displays the most common day transactions were made.
#It doesn't take into account the time transactions were made (Saturday night purchases technically are Sunday)
cd = df['Day'].mode()[0]
print("The most common day purchases were made is {}.".format(cd))
 
 
#The following displays the total amount spent for each day.

 
 
 
 
 
 
 
# def main():
#     while True:
     
#      values(df)
 
# if __name__ == "__main__":
# 	main()
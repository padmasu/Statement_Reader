'''This code will read through statements and will essentially output condensed versions'''
import pandas as pd
import time
import numpy as np
import csv


df = pd.read_csv(r"C:\Users\Phillipos Admasu\Documents\Statements\CSV\withdrawals.csv")
#df = pd.DataFrame(df)

df['Date'] = pd.to_datetime(df['Date'])

df['Day'] = df['Date'].dt.weekday_name 

print(df)
 
 
 
 
 
 
# def main():
#     while True:
     
#      values(df)
 
# if __name__ == "__main__":
# 	main()
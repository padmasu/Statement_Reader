'''This code will read through statements and will essentially output condensed versions'''
import pandas as pd
import time
import numpy as np
import csv
# d = {
#      "cars":["Ford","chevy"],
#      "food":"burgres"
#      }

# print(d)

infile = pd.read_csv(r"C:\Users\Phillipos Admasu\Documents\Statements\CSV\withdrawals.csv")
outfile = pd.read_csv(r"C:\Users\Phillipos Admasu\Documents\Statements\CSV\withdrawals.csv")

# with open(infile) as input:
#     reader = csv.reader(infile)
# with open(outfile) as output:
# 	writer = csv.writer(output)
# 	with_dict= {rows[3]:rows[4] for rows in reader}

statement_data = {'withdrawals': infile }

# deposits = pd.read_csv(r'C:\Users\Phillipos Admasu\Documents\Statements\CSV\deposits.csv')
# withdrawals = pd.read_csv(r'C:\Users\Phillipos Admasu\Documents\Statements\CSV\withdrawals.csv')

# months = ['january', 'february', 'march', 'april', 'may', 'june']
# days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
print(statement_data)
print(statement_data['197':"Venmo"])
#for item,cost in statement_data:
    













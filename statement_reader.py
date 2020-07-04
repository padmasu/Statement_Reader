'''This code will read through statements and will essentially output condensed versions'''
import pandas as pd
import time
import numpy as np


statement_data = { 'deposits': r'C:\Users\Phillipos Admasu\Documents\Statements\CSV\deposits.csv',
					'withdrawals': r'C:\Users\Phillipos Admasu\Documents\Statements\CSV\withdrawals.csv' }

deposits = pd.read_csv(r'C:\Users\Phillipos Admasu\Documents\Statements\CSV\deposits.csv')
withdrawals = pd.read_csv(r'C:\Users\Phillipos Admasu\Documents\Statements\CSV\withdrawals.csv')

months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

if "Venmo" in withdrawals:
	print("It's here!")
else:
	print("nope")



















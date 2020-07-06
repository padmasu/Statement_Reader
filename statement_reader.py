'''This code will read through statements and will essentially output condensed versions'''
import pandas as pd
import time
import numpy as np
import csv

def stat_reader(): 
	infile = pd.read_csv(r"C:\Users\Phillipos Admasu\Documents\Statements\CSV\withdrawals.csv")



	statement_data = {'withdrawals':infile}


	df = pd.DataFrame(data=statement_data)

	print(df.to_string(index=False))









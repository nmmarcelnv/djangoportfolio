#!/usr/bin/python

import pandas as pd

countries = pd.read_csv('../../country_names.csv')
countries = countries.set_index('country_code')

outf = open('load_disease_burden.py', 'a')

outf.write("\n")
for code in countries.index:
	outf.write("\t\t\tdisease_burden."+code+" = row['"+code+"']\n")


outf.close()

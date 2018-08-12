#!/usr/bin/python

import pandas as pd

countries = pd.read_csv('country_names.csv')
countries = countries.set_index('country_code')
#print(countries.head()) 

outf = open('models.py', 'w')

outf.write("from django.db import models\n\n")
outf.write("class Country(models.Model):\n\n")
outf.write("\tcountry_name = models.CharField(max_length=100, blank=False)\n")
outf.write("\tcountry_code = models.CharField(max_length=5, blank=False)\n")    
outf.write("\n\n\n")

outf.write("class DiseaseBurden(models.Model):\n\n")
outf.write("\tSex = models.CharField(max_length=50, blank=False)\n")
outf.write("\tGHEcode = models.IntegerField(max_length=50, blank=False)\n")
outf.write("\tGHEcause = models.CharField(max_length=50, blank=False)\n")
outf.write("\tDiseaseCategory = models.CharField(max_length=50, blank=False)\n")
outf.write("\tDiseaseName = models.CharField(max_length=100, blank=False)\n")
outf.write("\n")

for code in countries.index:
	outf.write("\t"+code+" = models.FloatField(max_length=20, blank=False)\n")


outf.close()

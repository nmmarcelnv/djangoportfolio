from csv import DictReader
from datetime import datetime
from django.core.management import BaseCommand
from diseases.models import Country
import pandas as pd

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload country data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
	# Show this when the user types help
	help = "Loads data from country_names.csv into our Country model"

	def handle(self, *args, **options):
		if Country.objects.exists():
			print('Country data already loaded...exiting.')
			print(ALREADY_LOADED_ERROR_MESSAGE)
			return
		print("Loading data for countries available")
		for row in DictReader(open('./diseases/country_names.csv')):
			country = Country()
			country.country_name = row['country_name']
			country.country_code = row['country_code']
			country.save()


	def LoadDiseaseBurden(self, *args, **options):
		if DiseaseBurden.objects.exists():
			print('Disease Burden data already loaded...exiting.')
			print(ALREADY_LOADED_ERROR_MESSAGE)
			return

		print("Loading data for disease burden") 
		
		data = pd.read_csv('./disease/GHE2015_Deaths_2000_country.csv', nrows=1)
		codes = data.columns[5:]

		for row in DictReader(open('./disease/GHE2015_Deaths_2000_country.csv')):
			disease_burden = DiseaseBurden()
			
			disease_burden.Sex = row['Sex']
			disease_burden.GHEcode = row['GHEcode']
			disease_burden.GHEcause = row['GHEcause']
			disease_burden.DiseaseCategory = row['Disease Category'] 
			disease_burden.DiseaseName = row['Disease Name']

			

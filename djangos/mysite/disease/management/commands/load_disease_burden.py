from csv import DictReader
from datetime import datetime
from django.core.management import BaseCommand
from disease.models import Country, DiseaseBurden
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
		for row in DictReader(open('./disease/country_names.csv')):
			country = Country()
			country.country_name = row['country_name']
			country.country_code = row['country_code']
			country.save()


		if DiseaseBurden.objects.exists():
			print('Disease Burden data already loaded...exiting.')
			print(ALREADY_LOADED_ERROR_MESSAGE)
			return

		print("Loading data for disease burden")
		df = pd.read_csv('./disease/GHE2015_Deaths_2000_country.csv') 
		for index in df.index:
			disease_burden = DiseaseBurden()
			
			disease_burden.Sex = df.loc[index, 'Sex']
			disease_burden.GHEcode = df.loc[index, 'GHEcode']
			disease_burden.GHEcause = df.loc[index, 'GHEcause']
			disease_burden.DiseaseCategory = df.loc[index, 'Disease Category'] 
			disease_burden.DiseaseName = df.loc[index, 'Disease Name']


			disease_burden.AFG = df.loc[index, 'AFG']
			disease_burden.ALB = df.loc[index, 'ALB']
			disease_burden.DZA = df.loc[index, 'DZA']
			disease_burden.AGO = df.loc[index, 'AGO']
			disease_burden.ATG = df.loc[index, 'ATG']
			disease_burden.ARG = df.loc[index, 'ARG']
			disease_burden.ARM = df.loc[index, 'ARM']
			disease_burden.AUS = df.loc[index, 'AUS']
			disease_burden.AUT = df.loc[index, 'AUT']
			disease_burden.AZE = df.loc[index, 'AZE']
			disease_burden.BHS = df.loc[index, 'BHS']
			disease_burden.BHR = df.loc[index, 'BHR']
			disease_burden.BGD = df.loc[index, 'BGD']
			disease_burden.BRB = df.loc[index, 'BRB']
			disease_burden.BLR = df.loc[index, 'BLR']
			disease_burden.BEL = df.loc[index, 'BEL']
			disease_burden.BLZ = df.loc[index, 'BLZ']
			disease_burden.BEN = df.loc[index, 'BEN']
			disease_burden.BTN = df.loc[index, 'BTN']
			disease_burden.BOL = df.loc[index, 'BOL']
			disease_burden.BIH = df.loc[index, 'BIH']
			disease_burden.BWA = df.loc[index, 'BWA']
			disease_burden.BRA = df.loc[index, 'BRA']
			disease_burden.BRN = df.loc[index, 'BRN']
			disease_burden.BGR = df.loc[index, 'BGR']
			disease_burden.BFA = df.loc[index, 'BFA']
			disease_burden.BDI = df.loc[index, 'BDI']
			disease_burden.KHM = df.loc[index, 'KHM']
			disease_burden.CMR = df.loc[index, 'CMR']
			disease_burden.CAN = df.loc[index, 'CAN']
			disease_burden.CPV = df.loc[index, 'CPV']
			disease_burden.CAF = df.loc[index, 'CAF']
			disease_burden.TCD = df.loc[index, 'TCD']
			disease_burden.CHL = df.loc[index, 'CHL']
			disease_burden.CHN = df.loc[index, 'CHN']
			disease_burden.COL = df.loc[index, 'COL']
			disease_burden.COM = df.loc[index, 'COM']
			disease_burden.COG = df.loc[index, 'COG']
			disease_burden.CRI = df.loc[index, 'CRI']
			disease_burden.CIV = df.loc[index, 'CIV']
			disease_burden.HRV = df.loc[index, 'HRV']
			disease_burden.CUB = df.loc[index, 'CUB']
			disease_burden.CYP = df.loc[index, 'CYP']
			disease_burden.CZE = df.loc[index, 'CZE']
			disease_burden.PRK = df.loc[index, 'PRK']
			disease_burden.COD = df.loc[index, 'COD']
			disease_burden.DNK = df.loc[index, 'DNK']
			disease_burden.DJI = df.loc[index, 'DJI']
			disease_burden.DOM = df.loc[index, 'DOM']
			disease_burden.ECU = df.loc[index, 'ECU']
			disease_burden.EGY = df.loc[index, 'EGY']
			disease_burden.SLV = df.loc[index, 'SLV']
			disease_burden.GNQ = df.loc[index, 'GNQ']
			disease_burden.ERI = df.loc[index, 'ERI']
			disease_burden.EST = df.loc[index, 'EST']
			disease_burden.ETH = df.loc[index, 'ETH']
			disease_burden.FJI = df.loc[index, 'FJI']
			disease_burden.FIN = df.loc[index, 'FIN']
			disease_burden.FRA = df.loc[index, 'FRA']
			disease_burden.GAB = df.loc[index, 'GAB']
			disease_burden.GMB = df.loc[index, 'GMB']
			disease_burden.GEO = df.loc[index, 'GEO']
			disease_burden.DEU = df.loc[index, 'DEU']
			disease_burden.GHA = df.loc[index, 'GHA']
			disease_burden.GRC = df.loc[index, 'GRC']
			disease_burden.GRD = df.loc[index, 'GRD']
			disease_burden.GTM = df.loc[index, 'GTM']
			disease_burden.GIN = df.loc[index, 'GIN']
			disease_burden.GNB = df.loc[index, 'GNB']
			disease_burden.GUY = df.loc[index, 'GUY']
			disease_burden.HTI = df.loc[index, 'HTI']
			disease_burden.HND = df.loc[index, 'HND']
			disease_burden.HUN = df.loc[index, 'HUN']
			disease_burden.ISL = df.loc[index, 'ISL']
			disease_burden.IND = df.loc[index, 'IND']
			disease_burden.IDN = df.loc[index, 'IDN']
			disease_burden.IRN = df.loc[index, 'IRN']
			disease_burden.IRQ = df.loc[index, 'IRQ']
			disease_burden.IRL = df.loc[index, 'IRL']
			disease_burden.ISR = df.loc[index, 'ISR']
			disease_burden.ITA = df.loc[index, 'ITA']
			disease_burden.JAM = df.loc[index, 'JAM']
			disease_burden.JPN = df.loc[index, 'JPN']
			disease_burden.JOR = df.loc[index, 'JOR']
			disease_burden.KAZ = df.loc[index, 'KAZ']
			disease_burden.KEN = df.loc[index, 'KEN']
			disease_burden.KIR = df.loc[index, 'KIR']
			disease_burden.KWT = df.loc[index, 'KWT']
			disease_burden.KGZ = df.loc[index, 'KGZ']
			disease_burden.LAO = df.loc[index, 'LAO']
			disease_burden.LVA = df.loc[index, 'LVA']
			disease_burden.LBN = df.loc[index, 'LBN']
			disease_burden.LSO = df.loc[index, 'LSO']
			disease_burden.LBR = df.loc[index, 'LBR']
			disease_burden.LBY = df.loc[index, 'LBY']
			disease_burden.LTU = df.loc[index, 'LTU']
			disease_burden.LUX = df.loc[index, 'LUX']
			disease_burden.MDG = df.loc[index, 'MDG']
			disease_burden.MWI = df.loc[index, 'MWI']
			disease_burden.MYS = df.loc[index, 'MYS']
			disease_burden.MDV = df.loc[index, 'MDV']
			disease_burden.MLI = df.loc[index, 'MLI']
			disease_burden.MLT = df.loc[index, 'MLT']
			disease_burden.MRT = df.loc[index, 'MRT']
			disease_burden.MUS = df.loc[index, 'MUS']
			disease_burden.MEX = df.loc[index, 'MEX']
			disease_burden.FSM = df.loc[index, 'FSM']
			disease_burden.MNG = df.loc[index, 'MNG']
			disease_burden.MNE = df.loc[index, 'MNE']
			disease_burden.MAR = df.loc[index, 'MAR']
			disease_burden.MOZ = df.loc[index, 'MOZ']
			disease_burden.MMR = df.loc[index, 'MMR']
			disease_burden.NAM = df.loc[index, 'NAM']
			disease_burden.NPL = df.loc[index, 'NPL']
			disease_burden.NLD = df.loc[index, 'NLD']
			disease_burden.NZL = df.loc[index, 'NZL']
			disease_burden.NIC = df.loc[index, 'NIC']
			disease_burden.NER = df.loc[index, 'NER']
			disease_burden.NGA = df.loc[index, 'NGA']
			disease_burden.NOR = df.loc[index, 'NOR']
			disease_burden.OMN = df.loc[index, 'OMN']
			disease_burden.PAK = df.loc[index, 'PAK']
			disease_burden.PAN = df.loc[index, 'PAN']
			disease_burden.PNG = df.loc[index, 'PNG']
			disease_burden.PRY = df.loc[index, 'PRY']
			disease_burden.PER = df.loc[index, 'PER']
			disease_burden.PHL = df.loc[index, 'PHL']
			disease_burden.POL = df.loc[index, 'POL']
			disease_burden.PRT = df.loc[index, 'PRT']
			disease_burden.QAT = df.loc[index, 'QAT']
			disease_burden.KOR = df.loc[index, 'KOR']
			disease_burden.MDA = df.loc[index, 'MDA']
			disease_burden.ROU = df.loc[index, 'ROU']
			disease_burden.RUS = df.loc[index, 'RUS']
			disease_burden.RWA = df.loc[index, 'RWA']
			disease_burden.LCA = df.loc[index, 'LCA']
			disease_burden.VCT = df.loc[index, 'VCT']
			disease_burden.WSM = df.loc[index, 'WSM']
			disease_burden.STP = df.loc[index, 'STP']
			disease_burden.SAU = df.loc[index, 'SAU']
			disease_burden.SEN = df.loc[index, 'SEN']
			disease_burden.SRB = df.loc[index, 'SRB']
			disease_burden.SYC = df.loc[index, 'SYC']
			disease_burden.SLE = df.loc[index, 'SLE']
			disease_burden.SGP = df.loc[index, 'SGP']
			disease_burden.SVK = df.loc[index, 'SVK']
			disease_burden.SVN = df.loc[index, 'SVN']
			disease_burden.SLB = df.loc[index, 'SLB']
			disease_burden.SOM = df.loc[index, 'SOM']
			disease_burden.ZAF = df.loc[index, 'ZAF']
			disease_burden.SSD = df.loc[index, 'SSD']
			disease_burden.ESP = df.loc[index, 'ESP']
			disease_burden.LKA = df.loc[index, 'LKA']
			disease_burden.SDN = df.loc[index, 'SDN']
			disease_burden.SUR = df.loc[index, 'SUR']
			disease_burden.SWZ = df.loc[index, 'SWZ']
			disease_burden.SWE = df.loc[index, 'SWE']
			disease_burden.CHE = df.loc[index, 'CHE']
			disease_burden.SYR = df.loc[index, 'SYR']
			disease_burden.TJK = df.loc[index, 'TJK']
			disease_burden.THA = df.loc[index, 'THA']
			disease_burden.MKD = df.loc[index, 'MKD']
			disease_burden.TLS = df.loc[index, 'TLS']
			disease_burden.TGO = df.loc[index, 'TGO']
			disease_burden.TON = df.loc[index, 'TON']
			disease_burden.TTO = df.loc[index, 'TTO']
			disease_burden.TUN = df.loc[index, 'TUN']
			disease_burden.TUR = df.loc[index, 'TUR']
			disease_burden.TKM = df.loc[index, 'TKM']
			disease_burden.UGA = df.loc[index, 'UGA']
			disease_burden.UKR = df.loc[index, 'UKR']
			disease_burden.ARE = df.loc[index, 'ARE']
			disease_burden.GBR = df.loc[index, 'GBR']
			disease_burden.TZA = df.loc[index, 'TZA']
			disease_burden.USA = df.loc[index, 'USA']
			disease_burden.URY = df.loc[index, 'URY']
			disease_burden.UZB = df.loc[index, 'UZB']
			disease_burden.VUT = df.loc[index, 'VUT']
			disease_burden.VEN = df.loc[index, 'VEN']
			disease_burden.VNM = df.loc[index, 'VNM']
			disease_burden.YEM = df.loc[index, 'YEM']
			disease_burden.ZMB = df.loc[index, 'ZMB']
			disease_burden.ZWE = df.loc[index, 'ZWE']
			#don't forget to save
			disease_burden.save()

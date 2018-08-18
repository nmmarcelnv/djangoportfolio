from django import forms
from .models import Country, DiseaseBurden 

import plotly
import plotly.graph_objs as go

class CountryForm(forms.Form):
    #create tuples (country_code, country_name) 
    countries = Country.objects.all()
    CHOICES = ((country.country_code, country.country_name) for country in countries)
    #post = forms.CharField()
    country = forms.ChoiceField(widget=forms.Select, choices=CHOICES)


class GraphForm:
	
	def __init__(self, country_code='USA'):

		self.country_code = country_code
		self.males = 'Males'
		self.females = 'Females'
		
	def make_figure(self):
		
		"""Returns list of top ten killer diseases
		for country with country_code.
		https://plot.ly/python/pie-charts/
		"""
		#collect data for males
		queryset1 = (	DiseaseBurden.objects.
				filter(Sex=self.males).
				order_by('-'+self.country_code)[:10]
			    )
 		
		deaths_males = [ dic[self.country_code] for dic in queryset1.values(self.country_code) ] 
		causes_males = [p.DiseaseName for p in queryset1 ] 

		#collect data for females
		queryset2 = (   DiseaseBurden.objects.
                                filter(Sex=self.females).
                                order_by('-'+self.country_code)[:10]
                            )
		deaths_females = [dic[self.country_code] for dic in queryset2.values(self.country_code) ] 
		causes_females = [p.DiseaseName for p in queryset2]


		fig = {
        		"data": [
        		{
                		"values": deaths_males,
                		"labels": causes_males,
                		"domain": {"x": [0, .48]},
                		"name": "Deaths",
                		"hoverinfo":"label+percent+name",
                		"hole": .4,
                		"type": "pie"
        		},
        		{
                		"values": deaths_females,
                		"labels": causes_females,
                		"text":["Female"],
                		"textposition":"inside",
                		"domain": {"x": [.50, 1]},
                		"name": "Deaths",
                		"hoverinfo":"label+percent+name",
                		"hole": .4,
                		"type": "pie"
        		}],

        		"layout": {
                	"title":"Cause of Deaths in "+self.country_code,
                	"annotations": [
                	{
                        	"font": {"size": 20},
                        	"showarrow": False,
                        	"text": "Males",
                        	"x": 0.22,
                        	"y": 0.5
                	},
                	{
                        	"font": {"size": 20},
                        	"showarrow": False,
                        	"text": "Females",
                        	"x": 0.78,
                        	"y": 0.5
                	} ]
        		}


        	}

		html_path = './disease/templates/disease/cause_of_death.html'
		plotly.offline.plot(fig,
                        filename = html_path,
                        show_link=True,
                        #output_type='div',
                        auto_open=False
                )

		return html_path

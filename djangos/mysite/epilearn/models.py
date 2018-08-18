from django.db import models
from django.forms import ModelForm

class SIRmodel(models.Model):

	R0 = models.FloatField(
		default=8.0, 
		verbose_name=' Basic Reproductive Number ')

	beta = models.FloatField(
		default=1.5, 
		verbose_name=' Rate of Infection        ')


class SIRmodelForm(ModelForm):
	class Meta:
		model = SIRmodel
		fields = "__all__"

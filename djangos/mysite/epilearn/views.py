from django.views.generic import TemplateView
from django.shortcuts import render, redirect

"""simple example of class-based view
we only need to provide a template to the variable template_name
Note: template_name is an internal variable used by TemplateView
"""

class EpilearnView(TemplateView):
    template_name = 'epilearn/index.html'


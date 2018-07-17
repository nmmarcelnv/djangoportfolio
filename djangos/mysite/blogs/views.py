from django.views.generic import TemplateView
from django.shortcuts import render, redirect


def TimeSeriesAnalysis(request):
    template_name = 'blogs/TimeSeriesAnalysis.html'
    return render(request, template_name)

def AdvancedTopicsMapApply(request):
    template_name = 'blogs/AdvancedTopicsMapApply.html'
    return render(request, template_name)

def BioStats1(request):
    template_name = 'blogs/BioStats1.html'
    return render(request, template_name)

def BioStats2(request):
    template_name = 'blogs/BioStats2.html'
    return render(request, template_name)

def BioStats3(request):
    template_name = 'blogs/BioStats3.html'
    return render(request, template_name)

def ReadingSaSDataSets(request):
    template_name = 'blogs/ReadingSaSDataSets.html'
    return render(request, template_name)

def ControllingInputOutputSAS(request):
    template_name = 'blogs/ControllingInputOutputSAS.html'
    return render(request, template_name)

def AppendConcatenate(request):
    template_name = 'blogs/AppendConcatenate.html'
    return render(request, template_name)

def AccumulateSAS(request):
    template_name = 'blogs/AccumulatingVariable.html'
    return render(request, template_name)

def Classification1(request):
    template_name = 'blogs/machinelearning1.html'
    return render(request, template_name)

def Classification2(request):
    template_name = 'blogs/machinelearning2.html'
    return render(request, template_name)

def JavaScript(request):
    template_name = 'blogs/JavaScript.html'
    return render(request, template_name)

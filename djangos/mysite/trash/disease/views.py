from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from disease.forms import CountryForm

"""simple example of class-based view
we only need to provide a template to the variable template_name
Note: template_name is an internal variable used by TemplateView
"""

class DiseaseView(TemplateView):
    template_name = 'disease/index.html'

    #Let's overwrite the get request method of TemplateView
    def get(self, request):
        #This renders a black form
        form = CountryForm()
        return render(request,self.template_name,{'form':form})

    plotfile = None
    def post(self, request):
        """This will render a form and fill it with the
            data received from the site.
        """
        form = CountryForm(request.POST)
        if form.is_valid():
            country = form.cleaned_data['country']
            plotfile = country+".png"
            #We could redirect the user to a new page
            #redirect('home:home')
        args = {'form':form, 'plotfile':plotfile}
        return render(request,self.template_name,args)

from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .models import SIRmodelForm
from . import SIRmodel as ode_solve
import os

"""simple example of class-based view
we only need to provide a template to the variable template_name
Note: template_name is an internal variable used by TemplateView
"""

class EpilearnView(TemplateView):
    template_name = 'epilearn/index.html'


class SIRmodelView(TemplateView):
    template_name = 'epilearn/SIRmodel.html'

    #Let's overwrite the get request method of TemplateView
    def get(self, request):
        #This renders a black form
        form = SIRmodelForm()
        return render(request, self.template_name, {'form':form})

    result = None
    def post(self, request):
        """This will render a form and fill it with the
            data received from the site.
        """
        form = SIRmodelForm(request.POST)

        if form.is_valid():

            form.save(commit=False) 
            
            R0 = form.cleaned_data['R0'] 
            beta = form.cleaned_data['beta']
            gamma = float(beta/R0) 

            #solve the SIR model with new parameters
       
            dir_path = os.path.dirname(os.path.realpath(__file__))
            #print(dir_path)
            filename = os.path.join(dir_path, 'static/epilearn/img/SImodel.png')

            result = ode_solve.interactive_plot(beta, gamma)
            #We could redirect the user to a new page
            #return redirect('https://www.tutorialspoint.com/django/django_page_redirection.htm')
        args = {'form':form, 'R0':R0, 'beta':beta, 'result':result}
        return render(request, self.template_name, args)



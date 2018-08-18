from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from home.forms import HomeForm

"""simple example of class-based view
we only need to provide a template to the variable template_name
Note: template_name is an internal variable used by TemplateView
"""

class HomeView(TemplateView):
    template_name = 'home/home.html'

    #Let's overwrite the get request method of TemplateView
    def get(self, request):
        #This renders a black form
        form = HomeForm()
        return render(request,self.template_name,{'form':form})

    def post(self, request):
        """This will render a form and fill it with the
            data received from the site.
        """
        form = HomeForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']
            choice = form.cleaned_data['choice_field']
            #We could redirect the user to a new page
            #redirect('home:home')
        args = {'form':form, 'text':text, 'choice':choice}
        return render(request,self.template_name,args)



def TimeSeriesAnalysis(request):
    template_name = 'home/TimeSeriesAnalysis.html'
    return render(request, template_name)

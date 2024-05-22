from django.shortcuts import render
 
# relative import of forms
from .models import AppModel
from .forms import AppForm
 
 
def create_view(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = AppForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "create_view.html", context)
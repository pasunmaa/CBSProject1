from django.shortcuts import render
 
# relative import of forms
from .models import TransactionModel
from .forms import TransactionForm
 
 
def create_view(request):
    # dictionary for initial data with 
    # field names as keys
    context = {}
 
    # add the dictionary during initialization
    form = TransactionForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form'] = form
    return render(request, "create_view.html", context)


def list_view(request):
    # dictionary for initial data with 
    # field names as keys
    context = {}
 
    # add the dictionary during initialization
    context["dataset"] = TransactionModel.objects.all() #.order_by("-id")
         
    return render(request, "list_view.html", context)


def detail_view(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["data"] = TransactionModel.objects.get(id = id)
         
    return render(request, "detail_view.html", context)
from django.shortcuts import render
from interactions.forms import ClientsForm


def form(request):
    form = ClientsForm()
    return render(request, 'clients_vz_form.html',{'form':form})
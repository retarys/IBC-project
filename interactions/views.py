from django.shortcuts import render
from .forms import ClientsForm, SnippetForm

def form(request):

    if request.method == 'POST':
        form = ClientsForm(request.POST)
        if form.is_valid():
            
            interaction_type = form.cleaned_data['interaction_type']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            comment = form.cleaned_data['comment']
            
            print(interaction_type,date,time,comment)

    form = ClientsForm()
    return render(request, 'clients_vz_form.html',{'form':form})


def snippet_detail(request):

    if request.method == 'POST':
        Modelform = SnippetForm(request.POST)
        if Modelform.is_valid():
            Modelform.save()

    Modelform = SnippetForm()
    return render(request, 'form.html',{'Modelform':Modelform})
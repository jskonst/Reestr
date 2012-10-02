# Create your views here.
from django.shortcuts import render_to_response
from forms import testForms
def contsct(request):
    if request.method=='POST':
        form=testForms(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            
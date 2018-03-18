from django.shortcuts import render
from . import forms
# Create your views here.
def index(request):
    return render(request,'homepage/index.html')

def coming_soon(request):
    return render(request,'comingsoon.html')

def register_form(request):
    form = forms.Owner_Reg()
    data={'reg_here':form}
    if request.method=='POST':
        form = forms.Owner_Reg(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request,'register/done.html',)

    return render(request,'register/register.html',context=data)

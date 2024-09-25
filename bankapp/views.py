from django.shortcuts import render,redirect
from .models import bank_tbl
from .forms import demo_form
# from django.urls import reverse

def read_(req):
    customer=bank_tbl.objects.all()
    return render(req,'bankapphtml/index.html',{'index': customer})

def add_(req):
    custfill=demo_form()
    if req.method == 'POST':
        custform=demo_form(req.POST)
        if custform.is_valid():
            custform.save()
        return redirect('index')
    return render(req,'bankapphtml/addcust.html',{'index': custfill})
        
def update_(req,ik):
    x=bank_tbl.objects.get(id=ik)
    y=demo_form(instance=x)
    if req.method == 'POST':
        y=demo_form(req.POST,instance=x)
        if y.is_valid():
            y.save()
        return redirect('index')
    return render(req,'bankapphtml/addcust.html',{'index': y })

def delete_(req,ik):
    x=bank_tbl.objects.get(id=ik)
    x.delete()
    return redirect('index')




# Create your views here.

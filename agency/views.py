
from django.shortcuts import render,redirect
from django.views.generic import View,FormView,CreateView,TemplateView,ListView
from .forms import CarForm
from account.models import CarList,orders
from django.utils.decorators import method_decorator
from company.urls import *

def signin_required(fn):
    def inner(request,*args, **kwargs):
        if request.user.is_authenticated:
            return fn(request,*args, **kwargs)
        else:
            return redirect("h")
    return inner


# Create your views here.
class AdminHomeView(TemplateView):
    template_name="adminhome.html"

class CarView(View):
    def get(self,request):
        form=CarForm()
        return render(request,"addcar.html",{"form":form})

    def post(self,request):
        form_data=CarForm(data=request.POST,files=request.FILES)
        if form_data.is_valid():
           form_data.save()
           return redirect("ah")
        return render(request,"addcar.html",{"form":form_data})

@method_decorator(signin_required,name="dispatch") 

class CarListView(ListView):
    template_name="carlists.html"
    queryset=CarList.objects.all()
    context_object_name="data"

@method_decorator(signin_required,name="dispatch") 
class CarEditView(ListView):
    def get(self,request,*args,**kwargs):
        cid=kwargs.get("id")
        ob=CarList.objects.get(id=cid)
        form=CarForm(instance=ob)
        return render(request,"editcars.html",{"form":form})
    def post(self,request,*args,**kwargs):
        cid=kwargs.get("id")
        ob=CarList.objects.get(id=cid)
        form_data=CarForm(data=request.POST,instance=ob)
        if form_data.is_valid():
            form_data.save()
            return redirect('carlist')
        return render(request,"editcars.html",{"form":form_data})

@method_decorator(signin_required,name="dispatch") 
class CarDelView(View):
    def get(self,request,*args,**kwargs):
        cid=kwargs.get("id")
        CarList.objects.filter(id=cid).delete()
        return redirect("carlist")
    
# class OrdersList(ListView):
#     template_name="orderlists.html"
#     def get()
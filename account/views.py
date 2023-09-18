from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,FormView,CreateView
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import *
from customer.urls import *
from django.contrib.auth import authenticate,login,logout


# Create your views here.

class LoginView(FormView):
    template_name="Mainhome.html"
    form_class=LoginForm
    
    def post(self,request,*args,**kwargs):
        form_data=LoginForm(data=request.POST)
        if form_data.is_valid():
            us=form_data.cleaned_data.get("username")
            pswd=form_data.cleaned_data.get("password")
            user=authenticate(request,username=us,password=pswd)
            if user is not None and user.is_superuser:
                login(request,user)
                messages.success(request,"Login Success!")
                return redirect('ah')
            elif user:
                login(request,user)
                messages.success(request,"Login Success!")
                return redirect('ch')
            else:
                messages.error(request,"Sign in failed!")
                return redirect('h')
        return render(request,"Mainhome.html",{"form":form_data})

class RegView(CreateView):
    template_name="regis.html"
    form_class=RegForm
    model=User
    success_url=reverse_lazy('h')

    def form_valid(self,form):
        messages.success(self.request,"Registered Successfully!")
        return super().form_valid(form)


class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect("h")

# @method_decorator(signin_required,name="dispatch") 
# class Search(View):
#     def get(self,request,*args,**kwargs):
#         search=request.GET.get("search")
#         car=CarList.objects.filter(car=search)
#         context={"searchpro":product}
#         return render(request,"search.html",context)

class AboutView(TemplateView):
   template_name='about.html'

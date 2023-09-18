from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View,ListView,DetailView,FormView
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from account.models import CarList,orders,PersonalDetModel
from .forms import *
from django.db.models import Q



def signin_required(fn):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            messages.error(request,"Login first!")
            return redirect("h")
    return inner

decs=[never_cache,signin_required]


class HomePage(TemplateView):
     template_name="Homepage.html"

@method_decorator(signin_required,name="dispatch") 
class CarsView(TemplateView):
    template_name="Viewcars.html"

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["data"]=CarList.objects.all()
        return context

class ComplaintView(View):
    template_name="postcomplaint.html"

    def get(self,request):
        form=ComplaintForm
        return render(request,"postcomplaint.html")
    

# Create your views here


class BookingView(View):
    template_name = 'car_booking_form.html'

    def get(self, request,*args,**kwargs):
        try:
            cid= kwargs.get("id")
            car = CarList.objects.get(id=cid)
            form = BookingForm()
        except car.DoesNotExist:
            messages.error(request, 'Car not found.')
            return redirect('ch')

        return render(request, self.template_name, {'car': car, 'form': form})

    def post(self, request, *args,**kwargs):
        try:
            cid= kwargs.get("id")
            car= CarList.objects.get(id=cid)
        except car.DoesNotExist:
            messages.error(request, 'Car not found.')
            return redirect('ch')

        form = BookingForm(request.POST)

        if form.is_valid():
            days = form.cleaned_data['days']
            pickdate = form.cleaned_data['pick_up']
            dropoff = form.cleaned_data['drop_off']
            overlapping_bookings = orders.objects.filter(
                car=car,
                days=days,
                pickdate=dropoff,
                dropoff=pickdate
            )

            if overlapping_bookings.exists():
                messages.error(request, 'This vehicle is unavailable for the selected dates.')
                return redirect('ch')
            if dropoff <= pickdate:
                messages.error(request, 'Invalid date selection. Check-out date must be after check-in date.')
                return render(request, self.template_name, {'car': car, 'form': form})
            filter_conditions = [Q(pickdate=pickdate), Q(dropoff=dropoff)]
            combined_condition = Q(car=car) & (filter_conditions[0] | filter_conditions[1])
            is_available = orders.objects.filter(combined_condition).exists()
            if is_available:
                 messages.error(request, 'This vehicle is unavailable for the selected dates.')
                 return redirect('ch')
            else:
                booking = orders(
                    user=request.user,  
                    car=car,
                    days=days,          
                    pickdate=pickdate,
                    dropoff=dropoff
                    )
                booking.save()
                print("booking >>>",booking.pk)
 
                messages.success(request, 'Thank you for booking with us!')
                return redirect('persdet',booking.pk)  
        else:
            messages.error(request, 'Invalid form data. Please check the form and try again.')
            
            return render(request, self.template_name, { 'car': car,'form': form})


class PaymentView(TemplateView):
    template_name="Payment.html"

class PersonDetView(View):
    template_name="userdetails.html"

    def get(self, request,id):
        # pid=kwargs.get("id")
        pid=id
        order=orders.objects.get(id=pid)
        od=order.id
        print("order",od)
        form = PersonalDet()
        return render(request, self.template_name, {'order':od,'form': form})

    def post(self,request,id):
        print("reached here post ",id)
        form = PersonalDet(request.POST)
        print("from data >>>",form)
        if form.is_valid():
            print("reached form")
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            pickad=form.cleaned_data['pickad']
            dropad = form.cleaned_data['dropad']
            picktym = form.cleaned_data['picktym']
            droptym = form.cleaned_data['droptym']
            print("datas>>>>>",name,phone,address,pickad,dropad,picktym,droptym)
            pid=id
            order=orders.objects.get(id=pid)
            ud=PersonalDetModel(
                order=order,
                name=name,
                phone=phone,
                address=address,
                pickad=pickad,
                dropad=dropad,
                picktym=picktym,
                droptym=droptym
            )
            ud.save()
            return redirect('pay')
        else:
            pid=id
            order=orders.objects.get(id=pid)
            od=order.id
            return render(request, self.template_name, {'order':od,'form': form})
            

    
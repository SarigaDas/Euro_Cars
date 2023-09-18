from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CarList(models.Model):
    name=models.CharField(max_length=500)
    seats=models.IntegerField()
    image=models.ImageField(upload_to='cars')
    features=models.CharField(max_length=500)
    rent=models.IntegerField()
    options=(
        ('Petrol','Petrol'),
        ('Diesel','Diesel'),
        ('Electric','Electric')
    )
    fuel=models.CharField(max_length=100,choices=options,default='Petrol')

class orders(models.Model):
    car=models.ForeignKey(CarList,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    days=models.IntegerField()
    date=models.DateField(auto_now_add=True)
    pickdate=models.DateField()
    dropoff=models.DateField()
    # location=models.PointField(geography=True, spatial_index=True)
    options=(
        ('Order placed','Order placed'),
        ('Delivered','Delivered'),
        ('Returned','Returned'),
        ('Cancelled','Cancelled')
    )
    status=models.CharField(max_length=100,choices=options,default="Order placed")
    is_available = models.BooleanField(default=True)

    # def save(self, *args, **kwargs):
    #     # Check for overlapping bookings before saving
    #     if self.is_overlapping():
    #         raise ValueError("Booking dates overlap with existing bookings.")
    #     super().save(*args, **kwargs)
    
    # def is_overlapping(self):
    #     overlapping_orders = orders.objects.filter(
    #         car=self.car,
    #         pickdate__lte=self.dropoff,
    #         dropoff__gte=self.pickdate,
    #     )
    #     return overlapping_orders.exists()

class Complaint(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    complaint=models.CharField(max_length=1000)
    reply=models.CharField(max_length=1000,default="Not Replied yet")
    date=models.DateField(auto_now_add=True)

class PersonalDetModel(models.Model):
    order=models.ForeignKey(orders,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    phone=models.IntegerField()
    address=models.CharField(max_length=500)
    pickad=models.CharField(max_length=500)
    dropad=models.CharField(max_length=500)
    picktym=models.TimeField()
    droptym=models.TimeField()

class UserInfo(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    phone=models.IntegerField()
    address=models.CharField(max_length=500)
    pickad=models.CharField(max_length=500)
    dropad=models.CharField(max_length=500)
    picktym=models.TimeField()
    droptym=models.TimeField()


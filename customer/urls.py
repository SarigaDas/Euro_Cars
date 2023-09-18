from django.urls import path
from .views import *



urlpatterns=[
    path('custh',HomePage.as_view(),name='ch'),
    path('carview',CarsView.as_view(),name='carview'),
    path('postcom',ComplaintView.as_view(),name='postcom'),
    path('carbook/<int:id>',BookingView.as_view(),name='carbook'),
    path('pay',PaymentView.as_view(),name='pay'),
    path('persdet/<int:id>',PersonDetView.as_view(),name='persdet')
    
    

]
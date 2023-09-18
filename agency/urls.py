from django.urls import path
from .views import *


urlpatterns=[
    path('car',CarView.as_view(),name='car'),
    path('adminhome',AdminHomeView.as_view(),name='ah'),
    path('carlist',CarListView.as_view(),name='carlist'),
    path('cardel/<int:id>',CarDelView.as_view(),name='cardel'),
    path('editcar/<int:id>',CarEditView.as_view(),name='editcar')
    
]
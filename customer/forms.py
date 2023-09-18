from django import forms
from account.models import *
from .models import *
from django.contrib.auth.models import User
from django.forms import ModelForm,Textarea



class BookingForm(forms.Form):
    days = forms.IntegerField()
    pick_up = forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))
    drop_off = forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))

    def clean(self):
        cleaned_data = super().clean()
        days = cleaned_data.get('days')
        pick_up = cleaned_data.get('pickdate')
        drop_off = cleaned_data.get('dropoff')

        if pick_up and drop_off and pick_up >= drop_off:
            raise forms.ValidationError("Drop off date must be after pickup date")

        return cleaned_data


class ComplaintForm(forms.ModelForm):
    class Meta:
        model=Complaint
        fields=['complaint']
        widgets={
            'complaint':Textarea(attrs={'cols': 80, 'rows': 20})
        }

class PersonalDet(forms.ModelForm):
    class Meta:
        model=PersonalDetModel
        fields=['name','phone','address','pickad','dropad','picktym','droptym']
        widgets = {
            'picktym': forms.TimeInput(attrs={'type': 'time'}),
            'droptym': forms.TimeInput(attrs={'type': 'time'}),
        }
    




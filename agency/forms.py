from django import forms
from account.models import CarList

class CarForm(forms.ModelForm):
    class Meta:
        model=CarList
        fields=['image','name','seats','features','fuel','rent']
        
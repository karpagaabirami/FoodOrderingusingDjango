from django import forms
from .models import customr
class customerform(forms.ModelForm):
    class Meta:
        model=customr
        fields=['name','age','phoneno','Emailid']

class custologin(forms.ModelForm):
    class Meta:
        model=customr
        fields=['Emailid','phoneno']
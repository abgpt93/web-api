from django import forms
from django.db.models import fields
from .models import User
#from django.core import validators

class UserForm(forms.ModelForm):
    name = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())   
    password_confirmation =  forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=('name','email','password','password_confirmation')

    def clean(self):
        cleaned_data=super(UserForm,self).clean()     #ensures that any validation logic in parent class is maintained
        password=cleaned_data.get("password")
        password_confirmation=cleaned_data.get("password_confirmation")
        
        if password != password_confirmation:
            self.add_error('confirm_password',"Password does not match")
            raise forms.ValidationError("Password Not matched")
        
        return cleaned_data

            


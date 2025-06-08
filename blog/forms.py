from django import forms
from .models import UserSignUp




class SigninForm(forms.Form):
    username = forms.CharField(max_length=100, required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    

class SiginUpForm(forms.ModelForm):
    class Meta:
        model = UserSignUp
        fields = ['user_name', 'phone_number', 'email', 'password']
        widgets = {
            'user_name': forms.TextInput(attrs={'placeholder': 'user name', 'class': 'border border-indigo-500 py-3 px-3 rounded-md outline-none bg-indigo-100 md:w-[20vw]'}),
            'phone_number': forms.NumberInput(attrs={'placeholder': 'phone number', 'class': 'border border-indigo-500 py-3 px-3 rounded-md outline-none bg-indigo-100 md:w-[20vw]'}),
            'email': forms.EmailInput(attrs={'placeholder': 'email', 'class': 'border border-indigo-500 py-3 px-3 rounded-md outline-none bg-indigo-100 md:w-[20vw]'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'password', 'class': 'border border-indigo-500 py-3 px-3 rounded-md outline-none bg-indigo-100 md:w-[20vw]'}),

        }


from django import forms
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from users.models import User

#class for the login
# class UserLoginForm(AuthenticationForm):

#     email = forms.CharField(widget=forms.EmailInput(
#         attrs={'class': 'bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none', 'type' : 'text' , 'placeholder': 'Email', 'id': 'email'}))
#     password = forms.CharField(widget=forms.PasswordInput(
#         attrs={'class': 'bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none', 'placeholder': 'Password', 'id': 'password'}))

#     def __init__(self, *args, **kwargs):
#         super(UserLoginForm, self).__init__(*args, **kwargs)

#         for fieldname in ["email", "password"]:
#             self.fields[fieldname].help_text = None
        
#     class Meta:
#         model = settings.AUTH_USER_MODEL
#         fields = ("email" , "password")
class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none', 'placeholder': 'Password', 'id': 'password'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none', 'placeholder': 'Password', 'id': 'password'}))

    
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if not email or not password:
            raise forms.ValidationError("You must enter both email and password.")
        
        return cleaned_data


#class for the register
class UserRegisterForm(UserCreationForm):

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none', 'type' : 'text' , 'placeholder': 'first_name', 'id': 'first_name'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none', 'type' : 'text' , 'placeholder': 'last_name', 'id': 'last_name'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none', 'type' : 'email' ,'placeholder': 'Email', 'id': 'email'})
    )
    password1 = forms.CharField(widget=forms.PasswordInput( 
        attrs={'class': 'bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none', 'placeholder': 'Password', 'id': 'password1'})
    )
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none', 'placeholder': 'Confirm', 'id': 'password2'})
    )

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        for fieldname in ["first_name","last_name", "email","password1", "password2"]:
            self.fields[fieldname].help_text = None
                    
    class Meta:
        model = User
        fields = ("first_name","last_name","email","password1", "password2")
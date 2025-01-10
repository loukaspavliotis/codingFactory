from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_active']
class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        error_messages={'required': 'Username is required.'}
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        error_messages={'required': 'Password is required.'}
    )
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("A user with that email already exists.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("A user with that username already exists.")
        return username

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        validate_password(password1)
        return password1
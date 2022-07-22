from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Student, Teacher
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username',)


class TeacherLoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(label='Password', max_length=30, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))


class StudentLoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(label='Password', max_length=30, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))

from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, help_text='')
    password2 = forms.CharField(label='Confirmation Password', widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['username', 'password1', 'password2',]
        
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''

    def clear_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            raise forms.ValidationError("Password Mismatch!")
        return self.cleaned_data['password2']


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


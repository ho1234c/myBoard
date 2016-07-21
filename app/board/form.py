from django import forms

from .models import Users, Posts


class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('name', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }
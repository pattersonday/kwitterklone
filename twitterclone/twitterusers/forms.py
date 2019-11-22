from django import forms


class AddTwitterUserForm(forms.Form):
    name = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

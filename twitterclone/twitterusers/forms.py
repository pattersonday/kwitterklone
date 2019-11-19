from django import forms


class AddTwitterForm(forms.Form):
    name = forms.CharField(max_length=50)
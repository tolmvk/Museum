from django import forms

class UserForm(forms.Form):
    like = forms.BooleanField(label="Он хорошо выглядит?")
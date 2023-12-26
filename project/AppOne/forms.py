from django import forms

from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder":"Enter your name"
            }),
            "address":forms.TextInput(attrs={
                 "class": "form-control",
                "placeholder":"Enter your Address"
            }),
            "age": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder":"Enter your Phone"
            })
        }
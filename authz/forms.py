from django import forms

from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

        error_messages = {
            "name": {
                "max_length": "Please enter a shorter name!",
                "min_length": "Password must contain atleast 2 characters!"
            },
            "email": {
                "invalid": "Please enter a valid email address!",
                "required": "Email field must not be empty!"
            },
            "password": {
                "min_length": "Password must contain atleast 6 characters!",
                "required": "Password field must not be empty!"
            }
        }
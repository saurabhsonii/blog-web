from django import forms
from .models import User  # Make sure to import your User model

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        # Exclude the fields you mentioned
        exclude = [
            'password',  # Password should be handled separately
            'last_login',
            'is_superuser',
            'groups',
            'user_permissions',
            'is_active',  # As you may want to control this programmatically
            'is_staff',  # As you may want to control this programmatically
            'created_at',  # These fields are managed automatically by Django
            'updated_at',
            'role'  # You may also want to handle role programmatically
        ]

    # Handle password field separately with proper input masking
    password = forms.CharField(widget=forms.PasswordInput, required=True)

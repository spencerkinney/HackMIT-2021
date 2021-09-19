from django import forms
from django.db import models
from .models import Profile, University
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)
import unicodedata
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.models import User

class UserCreationForm2(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
    }
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        first_name = models.CharField(_('username'), max_length=150, blank=True)
        first_name = models.CharField(_('first_name'), max_length=150, blank=True)
        phone_number = models.CharField(_('phone_number'), max_length=10, blank=True)
        University = models.ManyToManyField(University)
        profile_picture = models.ImageField(upload_to='pictures')
        model = Profile
        fields = ("username", "email", "phone_number", "first_name", "last_name","university","profile_picture",)
        field_classes = {'username' : forms.CharField, 'email': forms.EmailField, 'phone_number': forms.CharField, 'first_name': forms.CharField, 'last_name': forms.CharField, 'University':forms.MultipleChoiceField, "profile_picture":forms.ImageField}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
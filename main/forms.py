# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm


class Login_form(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "e.g: SteliosKarvanis",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "e.g: SecretP@ssword!",
                "class": "form-control"
            }
        ))

class Sign_up_form(UserCreationForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "e.g: SteliosKarvanis",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "e.g: SecretP@ssword!",
                "class": "form-control"
            }
        ))
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "e.g: SecretP@ssword!",
                "class": "form-control"
            }
        ))
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "e.g: stelioscbranco@hotmail.com",
                "class": "form-control"
            }
        ))
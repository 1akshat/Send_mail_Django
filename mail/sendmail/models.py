from django.db import models
from django import forms

class EmailForm(forms.Form):
	firstname = forms.CharField(max_length=255)
	lastname = forms.CharField(max_length=255)
	email = forms.EmailField()
	subject = forms.CharField(max_length=255)
	message = forms.CharField()

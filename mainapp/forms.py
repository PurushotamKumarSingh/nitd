from django import forms

from .models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact_ContactForm
        fields = ['name', 'email', 'subject', 'message']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'email', 'course', 'contact']

class QuoteRequestForm(forms.ModelForm):
    class Meta:
        model = Home_QuoteRequest
        fields = ['first_name', 'last_name', 'course_selection', 'phone', 'message']

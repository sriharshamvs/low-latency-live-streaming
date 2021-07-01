from django.db import models
from django.forms import ModelForm, Form
from .models import ContactDetail

class ContactDetailsForm(ModelForm):
    class Meta:
        model = ContactDetail
        fields = ['name','mobile_number','email_address','place']

        labels = {"place":"Institution"}

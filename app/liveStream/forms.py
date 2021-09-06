from django.db import models
from django.forms import ModelForm, Form
from .models import ContactDetail, ContactDetailFDP

class ContactDetailsForm(ModelForm):
    class Meta:
        model = ContactDetail
        fields = ['name','mobile_number','email_address','place']
        labels = {"place":"Institution"}

class ContactDetailFdpForm(ModelForm):
    class Meta:
        model = ContactDetailFDP
        fields = ['name', 'mobile_number', 'email_address', 'unique_id', 'department', \
         'institute', 'state_of_the_institute', 'country_of_the_institute']
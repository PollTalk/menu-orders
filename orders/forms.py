from django import forms
from django.forms import ModelForm, CheckboxInput
from .models import Order

class OrderTakingForm(forms.ModelForm):
	class Meta:
		model = Order

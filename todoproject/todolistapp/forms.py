from django import forms 
from django.forms import ModelForm
from .models import Todolist

class TodoForm(forms.ModelForm):


	title=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add A New task'}))
	class Meta:
		model=Todolist
		fields="__all__"
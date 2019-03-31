from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
	class Meta:
		model=Student
		fields=['reg_no','dept','semester','wallet','password']
class StudentRawForm(forms.Form):
	reg_no=forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Eg:16000"}))
	dept=forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Eg:CSE,EEE,ECE,ME,CE"}))
	semester=forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': "Eg:1,2,3..."}))
	wallet=forms.DecimalField(widget=forms.NumberInput())
	password=forms.CharField(widget=forms.TextInput())
	#Retypepassword=forms.CharField(widget=forms.TextInput())
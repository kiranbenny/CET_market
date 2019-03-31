from django.shortcuts import render

from .forms import StudentRawForm
from .models import Student
# Create your views here.
def student_create(request):
	my_form=StudentRawForm()
	if (request.method == 'POST'):
		my_form=StudentRawForm(request.POST)
		#if not my_form.password==my_form.Retypepassword:
			#raise ValidationError('Passwords must match')
		if my_form.is_valid():
			Student.objects.create(**my_form.cleaned_data)
		else:
			print(my_form.errors)
	context={'form':my_form}
	return render(request,"create.html",context)
def details(request):
	obj=Student.objects.all()
	context={
	"object_list" : obj
	}
	return render(request,"details.html",context)
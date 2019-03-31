from django.db import models
from student.models import Student


# Create your models here.
class Item(models.Model):
	mod=Student()
	item_name=models.CharField(max_length=30)
	owner=models.ForeignKey(Student,on_delete=models.CASCADE)
	price=models.DecimalField(decimal_places=2,max_digits=10)
	details=models.TextField(blank=False)
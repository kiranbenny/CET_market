from django.db import models

# Create your models here.
class Student(models.Model):
	reg_no=models.CharField(max_length=11,null=False)
	dept=models.CharField(max_length=4,null=False)
	semester=models.DecimalField(max_digits=1,decimal_places=0,null=False)
	wallet=models.DecimalField(max_digits=1000,decimal_places=2,null=False)
	password=models.CharField(max_length=20)

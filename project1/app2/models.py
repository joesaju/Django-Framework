from django.db import models

# Create your models here.
class employee(models.Model):
	emp_id = models.IntegerField(primary_key=True)
	emp_name = models.CharField(max_length=40)
	emp_dob = models.DateField()
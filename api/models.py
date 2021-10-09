from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    employee_code = models.IntegerField()
    department = models.CharField(max_length=50)

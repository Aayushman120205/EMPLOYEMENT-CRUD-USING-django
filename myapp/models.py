from django.db import models
from django.core.validators import RegexValidator


class Employee(models.Model):
    First_Name =models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Email = models.EmailField(unique=True)

    phone_validator = RegexValidator(
        regex=r'^(\+91)?\d{10}$',
        message="Enter a valid 10-digit number. Optional +91 at the start."
    )
    Password = models.CharField(max_length = 100)
    Contact = models.CharField(validators=[phone_validator],max_length=13,unique=True)

    Date_of_Joining = models.DateField()

    def __str__(self):
        return f"{self.First_Name} {self.Last_Name}"
    

class Department(models.Model):
    Emp_Name = models.OneToOneField('Employee', on_delete=models.CASCADE)
    Dep_Name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Dep_Name} - {self.Emp_Name.First_Name} {self.Emp_Name.Last_Name}"

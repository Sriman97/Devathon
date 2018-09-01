from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator
from django.utils import timezone

# Create your models here.
class Student(models.Model):
    regId = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=50)
    branch = models.CharField(max_length=30)
    year = models.CharField(max_length=10)
    mobile_number = PhoneNumberField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    bookId = models.CharField(max_length=30,primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=30)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class IssuedBook(models.Model):
    bookId = models.CharField(max_length=30)
    issued_by = models.CharField(max_length=30)
    current_status = models.BooleanField(default=True)
    reissues = models.IntegerField(default=1,validators=[MaxValueValidator(3)])
    issued_date = models.DateField(default=timezone.now())
    returned_date = models.DateField(blank=True)

    def __str__(self):
        return self.bookId


class Librarian(models.Model):
    libId = models.CharField(max_length=30)
    lib_name = models.CharField(max_length=100)
    mobile_number = PhoneNumberField

    def __str__(self):
        return self.lib_name



     



    from django.db import models
    from phonenumber_field.modelfields import PhoneNumberField
    from django.core.validators import MaxValueValidator
    from django.utils import timezone
    from datetime import datetime, timedelta
    from django.contrib.auth.models import User
    # Create your models here.
    class Student(models.Model):
        user = models.ForeignKey(User,on_delete=models.CASCADE)
        regId = models.CharField(max_length=30, primary_key=True)
        name = models.CharField(max_length=50)
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
        issued_date = models.DateField(auto_now=False, auto_now_add=False)
        returned_date = models.DateField(auto_now=False, auto_now_add=False)

        def __str__(self):
            return self.bookId


    class Librarian(models.Model):
        user = models.ForeignKey(User,on_delete=models.CASCADE)
        libId = models.CharField(max_length=30)
        lib_name = models.CharField(max_length=100)
        #mobile_number = PhoneNumberField()
        fine = models.IntegerField(default=0)
        def __str__(self):
            return self.lib_name

    class Librarian(models.Model):
        user = models.ForeignKey(User,on_delete=models.CASCADE)
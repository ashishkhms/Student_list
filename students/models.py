from django.db import models

# Create your models here.
class Students(models.Model) :
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    roll_no = models.IntegerField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    fullname = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    gender = models.CharField(choices=gender_choices, max_length=100)

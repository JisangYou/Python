from django.db import models


# Create your models here.

# class Blog(models.Model):
#     Title = models.CharField('TITLE', max_length = 50)
#     Content = models.TextField('CONTENT')
#
#     def __str__(self):
#         return self.Title

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=200,default='')
    subtitle=models.CharField(max_length=200,default='')
    auther=models.CharField(max_length=200,default='')
    is_read = models.BooleanField(default=False)


    def __str__(self):
        return self.title
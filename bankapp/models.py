from django.db import models

class bank_tbl(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    place=models.TextField(default='chennai')
    email=models.EmailField()
    dob=models.DateTimeField()
    def __str__(self):
        return self.name

# Create your models here.

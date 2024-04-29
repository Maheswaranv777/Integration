from django.db import models


class mars(models.Model):
    name=models.CharField(max_length=100, null=False,blank=False)
    role=models.CharField(max_length=50,null=False,blank=False)
    age=models.IntegerField()

    def __str__(self):
        return self.name


# Create your models here.

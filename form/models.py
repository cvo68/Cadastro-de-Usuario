from django.db import models


class Form(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    birth = models.DateField()
    email = models.CharField(max_length=100)
    
    def __str__(self):
        return self.model
        
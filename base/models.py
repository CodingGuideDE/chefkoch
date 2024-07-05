from django.db import models
#from django.db.models import 

# Create your models here.
class Recipe(models.Model):
    #user = models.User
    #image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    createdAt = models.DateField(auto_now=True)

class Step(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)


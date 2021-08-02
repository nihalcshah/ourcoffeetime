from django.db import models

# Create your models here.
class TestResults(models.Model):
    description = models.CharField(max_length=5000)

    def __str__(self):
        return self.description


class TypesOfPlaces(models.Model):
    name = models.CharField(max_length=300)
    

    def __str__(self):
        return self.name
class Question(models.Model):
    question = models.CharField(max_length=1000)
    style = models.CharField(max_length=1000, default="_")
    previous = models.BooleanField(default=False)
    ty = models.ManyToManyField(TypesOfPlaces)
    
    def __str__(self):
        return self.style

class SearchServices(models.Model):
    location = models.CharField(max_length=1000, default="Fairfax")
    places = models.CharField(max_length=5000, default="")
    name = models.CharField(max_length=5000, default="_")


# class TypesOfPlaces(models.Model):
#     question = models.CharField(max_length=1000)
#     one = models.CharField(max_length=100, default="Food")
#     two = models.CharField(max_length=100, default="Games and Arcades")
#     three = models.CharField(max_length=100, default="Drinks")
#     four = models.CharField(max_length=100, default="Parks")
#     five = models.CharField(max_length=100, default="Historical Landmarks")
#     six = models.CharField(max_length=100, default="Hotels")
#     seven = models.CharField(max_length=100, default="Hikes")
#     eight = models.CharField(max_length=100, default="Beaches")
#     nine = models.CharField(max_length=100, default="Malls")

#     def 

from django.db import models

from django.db import models


# Create your models here.
class SpecialDiet(models.Model):

    diet = models.CharField(max_length=20 ,null=True)

    def __str__(self):
        return self.diet


class User(models.Model):
    male = 'M'
    female = 'F'
    SEX_CHOICES = [(male, 'Male'), (female, 'Female')]
    # id
    email = models.CharField(max_length=30, unique=True)
    # username
    username = models.CharField(blank=False, max_length=20, unique=True)
    # password
    password = models.CharField(max_length=20, blank=False)
    age = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default=male, null=True)
    height = models.IntegerField(blank=True, null=True)
    diet = models.ManyToManyField('SpecialDiet', blank=True)

    def __str__(self):
        return self.username


class Food(models.Model):
    title = models.CharField(max_length=100)
    rating = models.FloatField(max_length=9, blank=True, null=True)
    diet = models.ManyToManyField('SpecialDiet', blank=True)
    calories = models.IntegerField(blank=True, null=True)
    fat = models.IntegerField(blank=True, null=True)
    sodium = models.IntegerField(blank=True, null=True)
    protein = models.IntegerField(blank=True, null=True)
    image = models.CharField(max_length=100,null=True,blank=True,)

    def __str__(self):
        return self.title

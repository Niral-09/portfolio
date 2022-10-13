from distutils.command import upload
from unittest.util import _MAX_LENGTH
from django.db import models

class Home(models.Model):
    name = models.CharField(max_length = 20)
    greetings_1 = models.CharField(max_length = 20)
    greetings_2 = models.CharField(max_length = 20)
    photo = models.ImageField(upload_to ='photo/')
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

class About(models.Model):
    heading = models.CharField(max_length = 20)
    career = models.CharField(max_length = 200)
    description = models.TextField(blank = False)
    profile_img = models.ImageField(upload_to ='profile/')
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.career

class Profile(models.Model):
    about = models.ForeignKey(About,on_delete = models.CASCADE)
    social_name = models.CharField(max_length = 10)
    link = models.URLField(max_length = 1000)

class Category(models.Model):
    name = models.CharField(max_length = 20)
    updated = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name

class Skills(models.Model):
    category = models.ForeignKey(Category,on_delete = models.CASCADE)
    skil_name = models.CharField(max_length = 20)

class Portfolio(models.Model):
    image = models.ImageField(upload_to = 'portfolio/')
    link = models.CharField(max_length = 200)

    def __str__(self):
        return f'portfolio{self.link}'

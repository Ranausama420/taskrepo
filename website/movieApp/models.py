from django.db import models
from django.contrib import admin

class moviedata(models.Model):
     name= models.TextField()
     description= models.TextField()
     imgPath= models.TextField()
     duration= models.IntegerField()
     genre= models.TextField()
     language= models.TextField()
     mpaaRating= models.TextField()
     userRating= models.TextField()

     def __str__(self):
          return self.name

admin.site.register(moviedata)

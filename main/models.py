from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    #fields for book table
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    release_date = models.DateField()
    averageRating = models.FloatField(default=0)
    image = models.URLField(default=None, null=True)

    def __str__(self):
        return self.name
    
    def __unicode__(self):
        return self.name

class Review(models.Model):
    #fields for review table
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=5000)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.user.username

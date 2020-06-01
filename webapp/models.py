from django.db import models

class usrs(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=100)
    def __str__(self):
        return self.Name
class Event(models.Model):
    Email = models.CharField(max_length=50)
    Date = models.DateTimeField(auto_now_add=True)
    Title = models.CharField(max_length=200)
    Description = models.CharField(max_length=200)
    def __str__(self):
        return self.Title
class Event1(models.Model):
    Email = models.CharField(max_length=50)
    Date = models.DateTimeField(auto_now_add=True)
    Title = models.CharField(max_length=200)
    Description = models.CharField(max_length=200)



from django.db import models
from django.urls import reverse

# Create your models here.

class Class(models.Model):
    workoutdate = models.DateField()
    instructor = models.CharField(max_length=50)
    classlength = models.IntegerField()
    title = models.CharField(max_length=250)
    classdate = models.DateField()
    totoutput = models.IntegerField()
    avgoutput = models.IntegerField()
    avgresistance = models.IntegerField()
    avgcadence = models.IntegerField()
    distance = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.instructor + '' + self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'class_id': self.id})
    
    class Meta:
        ordering = ('-workoutdate',)

class Artist(models.Model):
    artist = models.CharField(max_length=100)
    pelclass = models.ForeignKey(Class, on_delete=models.CASCADE)
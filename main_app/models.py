from django.db import models

# Create your models here.

class Class(models.Model):
    workoutdate = models.DateField()
    instructor = models.CharField(max_length=50)
    classlength = models.IntegerField()
    title = models.CharField(max_length=250)
    classdate = models.DateField()
    totoutput = models.IntegerField()
    avgoutput = models.IntegerField()
    avgresistance = models.DecimalField(max_digits=2, decimal_places=2)
    avgcadence = models.IntegerField()
    distance = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.CharField(max_length=500)

    def __str__(self):
        return self.instructor + '' + self.title


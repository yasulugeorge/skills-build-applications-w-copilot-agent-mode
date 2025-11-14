from djongo import models

class Activity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    points = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

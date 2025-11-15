from djongo import models

class Workout(models.Model):
    user = models.CharField(max_length=100)
    activity = models.CharField(max_length=100)
    duration = models.IntegerField(help_text='Duration in minutes')
    date = models.DateField()
    
    def __str__(self):
        return f"{self.user} - {self.activity}"

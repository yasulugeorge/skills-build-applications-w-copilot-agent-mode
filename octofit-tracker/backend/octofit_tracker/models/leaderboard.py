from djongo import models

class Leaderboard(models.Model):
    user = models.CharField(max_length=100)
    team = models.CharField(max_length=50)
    points = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.user} - {self.points}"

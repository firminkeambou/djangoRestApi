from django.db import models

# Create your models here.
class Moviedata(models.Model):
    # by  default, when you query this model, it will returns with  "object", if you want a different behavior, for example the name of the movie, Do as follows:
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200)
    duration =  models.FloatField()
    rating = models.FloatField()
    
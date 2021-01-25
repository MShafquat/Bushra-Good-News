from djongo import models


# Create your models here.
class News(models.Model):
    headline = models.CharField(max_length=250)
    time = models.TimeField()
    description = models.CharField(max_length=500, null=True)
    image = models.ImageField(null=True)
    author = models.CharField(max_length=500)
    body = models.TextField()


from djongo import models


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=250)
    pubdate = models.TimeField()
    description = models.CharField(max_length=500, null=True)
    author = models.CharField(max_length=500)
    language = models.CharField(max_length=50)
    url = models.URLField(max_length=500)
    image = models.ImageField(null=True)
    body = models.TextField()

    def __str__(self):
        return self.title


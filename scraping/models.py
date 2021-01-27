from djongo import models
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

TITLE_WEIGHT = 0.7
BODY_WEIGHT = 0.3


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=250)
    pubdate = models.TimeField()
    description = models.CharField(max_length=500, null=True)
    author = models.CharField(max_length=500)
    language = models.CharField(max_length=50)
    url = models.URLField(max_length=500)
    image_url = models.URLField(max_length=500, null=True)
    body = models.TextField()

    def __str__(self):
        return self.title

    def is_positive(self):
        """
        checks if a news is positive
        :return: Boolean value (True/False)
        """

        title_polarity = analyzer.polarity_scores(self.title)['compound']
        body_polarity = analyzer.polarity_scores(self.body)['compound']
        news_polarity = body_polarity * BODY_WEIGHT + title_polarity * TITLE_WEIGHT
        return news_polarity >= 0

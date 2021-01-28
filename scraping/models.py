from djongo import models
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()


class News(models.Model):
    title = models.CharField(max_length=250, db_index=True, unique=True)
    pubdate = models.TimeField()
    description = models.CharField(max_length=500, null=True)
    author = models.CharField(max_length=500)
    language = models.CharField(max_length=50)
    url = models.URLField(max_length=500)
    image_url = models.URLField(max_length=500, null=True)
    body = models.TextField()

    def __str__(self):
        return self.title

    @property
    def is_positive(self):
        """
        checks if a news is positive
        :return: Boolean value (True/False)
        """

        title_polarity = analyzer.polarity_scores(self.title)['compound']
        return title_polarity >= 0

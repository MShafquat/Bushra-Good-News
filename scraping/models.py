from djongo import models
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()


class News(models.Model):
    title = models.CharField(max_length=250, db_index=True, unique=True)
    pubdate = models.DateTimeField()
    description = models.CharField(max_length=500, blank=True)
    author = models.CharField(max_length=500)
    language = models.CharField(max_length=50)
    url = models.URLField(max_length=500)
    image_url = models.URLField(max_length=500, blank=True)
    body = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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

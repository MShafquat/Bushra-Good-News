from textblob import TextBlob

HEADLINE_WEIGHT = 0.7
BODY_WEIGHT = 0.3


def is_positive(headline, body):
    """
    checks if a news is positive
    :param headline: headline of the news
    :param body: body of the news
    :return: Boolean value (True/False)
    """

    headline = TextBlob(headline)
    avg_headline_polarity = sum([sentence.sentiment.polarity for sentence in headline.sentences]) / len(
        headline.sentences)
    body = TextBlob(body)
    avg_body_polarity = sum([sentence.sentiment.polarity for sentence in body.sentences]) / len(body.sentences)
    news_polarity = avg_body_polarity * BODY_WEIGHT + avg_headline_polarity * HEADLINE_WEIGHT
    return news_polarity >= 0

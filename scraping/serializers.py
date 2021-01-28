from scraping.models import News
from rest_framework import serializers


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['title', 'url', 'pubdate', 'description', 'author', 'language', 'url', 'image_url', 'body']

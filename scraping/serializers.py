from scraping.models import News
from rest_framework import serializers


class NewsSerializer(serializers.ModelSerializer):
    is_positive = serializers.ReadOnlyField()

    class Meta:
        model = News
        fields = '__all__'

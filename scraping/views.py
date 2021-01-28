from rest_framework import viewsets
from scraping.models import News
from scraping.serializers import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow news to be viewed
    """
    queryset = News.objects.all().order_by('-pubdate')
    serializer_class = NewsSerializer

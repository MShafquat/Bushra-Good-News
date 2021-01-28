from rest_framework import viewsets
from scraping.models import News
from scraping.serializers import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow news to be viewed
    """
    id_list = [news.id for news in News.objects.all().order_by('-pubdate') if news.is_positive()]
    queryset = News.objects.filter(id__in=id_list)
    serializer_class = NewsSerializer

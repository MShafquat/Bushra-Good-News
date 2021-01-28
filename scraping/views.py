from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from scraping.models import News
from scraping.serializers import NewsSerializer
from django.core.management import call_command


class NewsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow news to be viewed
    """
    queryset = News.objects.all().order_by('-pubdate')
    serializer_class = NewsSerializer

    @action(detail=False, permission_classes=[IsAdminUser])
    def scrape_news(self, request):
        call_command('scrape')
        return Response(status=status.HTTP_202_ACCEPTED)

from django.core.management.base import BaseCommand

from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

from scraping.models import News


class Command(BaseCommand):
    help = "Collect news"

    def handle(self, *args, **options):
        pass

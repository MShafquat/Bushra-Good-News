from django.core.management.base import BaseCommand
from scraping.utils import daily_star


class Command(BaseCommand):
    help = "Collect news"

    def handle(self, *args, **options):
        daily_star.scrape()

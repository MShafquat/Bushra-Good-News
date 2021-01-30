from django.shortcuts import render
from django.views.generic import ListView, DetailView

from scraping.models import News


class NewsListView(ListView):
    model = News
    ordering = ['-pubdate']
    template_name = 'frontend/news_list.html'
    paginate_by = 10


class NewsDetailView(DetailView):
    model = News
    template_name = 'frontend/news_detail.html'

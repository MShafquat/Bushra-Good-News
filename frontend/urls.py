from django.urls import path

from frontend.views import NewsListView, NewsDetailView

urlpatterns = [
    path('', NewsListView.as_view()),
    path('news/<int:pk>', NewsDetailView.as_view(), name='news-detail'),
]

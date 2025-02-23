from django.urls import path

from apps.news.api.v1.views.views import get_news_data

urlpatterns = [
    path("news/", get_news_data, name="news"),
]

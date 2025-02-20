from django.urls import path

from apps.news.views import news_by_country_and_category, index

urlpatterns = [
    path("", index, name="index"),
    path("search/", news_by_country_and_category, name="news_by_country_and_category"),
]

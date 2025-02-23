from newsapi import NewsApiClient

from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.conf import settings

from apps.news.api.v1.serializers.serializers import NewsSerializer

from utils.constants import available_countries
from utils.helpers import get_full_country_name


@api_view(["GET"])
def get_news_data(request):
    newsapi = NewsApiClient(api_key=settings.NEWS_API_KEY)

    serializer = NewsSerializer(data=request.query_params)
    serializer.is_valid(raise_exception=True)
    country = serializer.validated_data.get("country")
    category = serializer.validated_data.get("category")

    try:
        if available_countries.get(country) is None:
            return Response(
                {
                    "error": f"No news found for your country {get_full_country_name(country)}."
                },
            )
        top_headlines = newsapi.get_top_headlines(
            category=category,
            language="en",
            country=country,
        )
        print(top_headlines)
        news_status = top_headlines["status"]
        if news_status == "error":
            return Response(
                {"error": top_headlines["message"]},
            )
        if news_status == "ok" and top_headlines["totalResults"] == 0:
            return Response(
                {
                    "error": f"No news found for {category} in {get_full_country_name(country)}."
                },
            )

        articles = top_headlines["articles"]
        context = []
        for article in articles:
            context.append(
                {
                    "title": article["title"],
                    "author": article["author"],
                    "description": article["description"],
                    "url": article["url"],
                    "image": article["urlToImage"],
                    "published_at": article["publishedAt"].split("T")[0],
                }
            )
        return Response(
            {
                "news_data": context,
                "message": f"Top headlines for {category} in {get_full_country_name(country)}.",
            }
        )

    except Exception as e:
        return Response(
            {"error": f"An error occurred: {e}"},
        )

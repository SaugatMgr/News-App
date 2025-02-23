import requests

from newsapi import NewsApiClient

from django.shortcuts import render
from django.conf import settings

from utils.constants import available_countries
from utils.helpers import get_full_country_name


def get_top_headlines(country, category, newsapi):
    try:
        if available_countries.get(country) is None:
            return {
                "error": f"No news found for your country {get_full_country_name(country)}."
            }
        top_headlines = newsapi.get_top_headlines(
            category=category,
            language="en",
            country=country,
        )
        status = top_headlines["status"]
        if status == "error":
            return {"error": top_headlines["message"]}
        if status == "ok" and top_headlines["totalResults"] == 0:
            return {
                "error": f"No news found for {category} in {get_full_country_name(country)}."
            }

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
        return {
            "news_data": context,
            "message": f"Top headlines for {category} in {get_full_country_name(country)}.",
        }
    except Exception as e:
        if str(e) == "invalid country":
            return {
                "error": f"No news found for your country {get_full_country_name(country)}."
            }
        return {"error": f"An error occurred: {e}"}


def index(request):
    user_location_data = requests.get("https://ipinfo.io/json").json()
    country_code = user_location_data["country"].lower()

    newsapi = NewsApiClient(api_key=settings.NEWS_API_KEY)
    context = get_top_headlines(country_code, "general", newsapi)

    return render(request, "news_display.html", context)


def news_by_country_and_category(request):
    get_request = request.GET
    country = get_request["country"]
    category = get_request["category"]

    newsapi = NewsApiClient(api_key=settings.NEWS_API_KEY)
    context = get_top_headlines(country, category, newsapi)

    return render(request, "news_display.html", context)

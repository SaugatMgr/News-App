import requests

from newsapi import NewsApiClient

from django.shortcuts import render
from django.conf import settings

from utils.constants import available_country_codes


def get_top_headlines(country, category, newsapi):
    try:
        if country not in available_country_codes:
            return {"error": "No news found for your country."}
        top_headlines = newsapi.get_top_headlines(
            category=category,
            language="en",
            country=country,
        )
        status = top_headlines["status"]
        if status == "error":
            return {"error": top_headlines["message"]}
        if status == "ok" and top_headlines["totalResults"] == 0:
            return {"error": f"No news found for {category} in {country}."}

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
                    "published_at": article["publishedAt"],
                }
            )
        return {"news_data": context}
    except Exception as e:
        if str(e) == "invalid country":
            return {"error": "No news found for your country."}
        return {"error": f"An error occurred: {e}"}


def index(request):
    user_location_data = requests.get("https://ipinfo.io/json").json()
    country_code = user_location_data["country"].lower()

    newsapi = NewsApiClient(api_key=settings.NEWS_API_KEY)
    context = get_top_headlines(country_code, "general", newsapi)

    return render(request, "user_location_news.html", context)


def news_by_country_and_category(request):
    get_request = request.GET
    country = get_request["country"]
    category = get_request["category"]

    newsapi = NewsApiClient(api_key=settings.NEWS_API_KEY)
    context = get_top_headlines(country, category, newsapi)

    return render(request, "news_results.html", context)

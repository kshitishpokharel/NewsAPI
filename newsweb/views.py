from django.shortcuts import render
import requests
import json


# Create your views here.
def home(request):
    news_api_request = requests.get(
        "https://newsapi.org/v2/top-headlines?language=en&pagesize=20&apiKey=?")
    news_api = json.loads(news_api_request.content)
    return render(request, 'home.html', {'news_api': news_api})


def sports(request):
    sports_news_api_request = requests.get(
        "https://newsapi.org/v2/top-headlines?category=sports&language=en&pagesize=30&apiKey"
        "=? "
        )
    sports_api = json.loads(sports_news_api_request.content)
    return render(request, 'sports.html', {'sports_api': sports_api})


def business(request):
    business_news_api_request = requests.get(
        "https://newsapi.org/v2/top-headlines?category=business&language=en&apiKey"
        "=?")
    business_api = json.loads(business_news_api_request.content)
    return render(request, 'business.html', {'business_api': business_api})


def scitech(request):
    sci_tech_api_request = requests.get(
        "https://newsapi.org/v2/top-headlines?(category=science OR "
        "category=technology)&language=en&apiKey=?")
    sci_tech_api = json.loads(sci_tech_api_request.content)
    return render(request, 'scitech.html', {'sci_tech_api': sci_tech_api})

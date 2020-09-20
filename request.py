from app import app
import urllib.request,json
from app.models import news

News = news.News 


#api key

api_key = app.config['NEWS_API_KEY']


base_url = app.config['NEWS_API_BASE_URL']



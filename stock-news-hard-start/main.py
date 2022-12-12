import requests
import smtplib
import os

# if on work run this shit in udemy folder
# otherwise get the keys from the websites

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

MY_EMAIL = "morriseberhard11@gmail.com"
PASSWORD = "in google"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


STOCK_KEY = os.environ.get("STOCKAPI_KEY")
NEWS_KEY = os.environ.get("NEWSAPI_KEY")
print(NEWS_KEY)

print(NEWS_KEY)
parameters_stock = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "datatype": "json",
    "apikey": str(STOCK_KEY)
}

response_stock = requests.get(STOCK_ENDPOINT, params=parameters_stock)
data_stock = response_stock.json()
dict_data = dict(data_stock["Time Series (Daily)"])
close_list = [value["4. close"] for (key, value) in dict_data.items()]

closing_price_yd = close_list[0]
closing_price_before_yd = close_list[1]

five_perc = 0.05 * float(closing_price_yd)
diff = float(closing_price_yd) - float(closing_price_before_yd)
diff_perc = round(((diff / float(closing_price_yd)) * 100), 2)
up_down = None

if diff > 0:
    up_down = "📈"
else:
    up_down = "📉"

if abs(diff) > five_perc:

    parameters_news = {
        "apiKey": str(NEWS_KEY),
        "q": "tesla",
        "sortBy": "publishedAt",
        "language": "en",
        "searchIn": "title"

    }

    response_news = requests.get(NEWS_ENDPOINT, params=parameters_news)
    data_news = response_news.json()
    three_articles = data_news["articles"][:3]
    formatted_article = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    article_title = [f'{article["title"]}' for article in three_articles]
    for article in formatted_article:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="morriseberhard44@gmail.com", msg=f"Subject:{COMPANY_NAME}: {diff_perc}%{up_down}\n\n{article}")


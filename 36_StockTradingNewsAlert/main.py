import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "PKPK9X5H4L02RIXW"
NEWS_API_KEY = "684d433235f24793ae84f5fa9c7acbb4"

TWILIO_SID = "ACefadaa80327dd9be51282ece211d2027"
TWILIO_AUTH_TOKEN = "d4851a9f8ee6a05b429b71951e2bc9f8"
sender = "+19707174283"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
    }

paramenters2 = {
    "q":COMPANY_NAME,
    "from":"2022-6-8",
    "to":"2022-6-5",
    "apiKey":NEWS_API_KEY
    }

response = requests.get(STOCK_ENDPOINT, params=parameters)
data = response.json()["Time Series (Daily)"]
print(data)
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_prince = float(yesterday_data["4. close"])
day_before_yesterday = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday["4. close"])
diference_close_price = abs(yesterday_closing_prince - day_before_yesterday_closing_price)
porcentage = ((yesterday_closing_prince*100)/day_before_yesterday_closing_price)-100
print(porcentage)
if abs(porcentage) > 0:
    news_response = requests.get(NEWS_ENDPOINT, params=paramenters2)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    # print("three_articles")
    # print(three_articles)
    # print("formatted_articles")
    # print(formatted_articles)
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        print(article)
        print(formatted_articles)
        message = client.messages.create(
            body=article,
            from_=sender,
            to="+541154077378",
        )

#Optional TODO: Format the message like this: 

# """
# TSLA: 🔺2%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds 
# and prominent investors are required to file by the SEC The 13F filings show the 
# funds' and investors' portfolio positions as of March 31st, near the height of 
# the coronavirus market crash.
# or
# "TSLA: 🔻5%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and 
# prominent investors are required to file by the SEC The 13F filings show the funds'
 # and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# """


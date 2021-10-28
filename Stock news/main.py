import requests
from datetime import date, timedelta
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_KEY = "Z18OHUV0B67QEQ89"
NEWS_APPI_KEY = "bafcbdd89d98401498918cb464d4f5b7"
TWILIO_SID = "TWILIOSID"
TWILIO_AUTH_TOKEN = "TWILIOTOKEN"

current_day = str(date.today())

parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_KEY,
}



response = requests.get(STOCK_ENDPOINT, parameters)
response.raise_for_status()
data = response.json()
current_day = date.today()
yesterday = str(current_day - timedelta(1))
open_tsla = float(data["Time Series (Daily)"][yesterday]["1. open"])
close_tsla_yesterday = float(data["Time Series (Daily)"][yesterday]["4. close"])

# print(open_tsla)
# print(close_tsla)



    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_closed = str(current_day - timedelta(2))
day_BY_close_tsla = float(data["Time Series (Daily)"][day_before_yesterday_closed]["4. close"])

# print(day_BY_close_tsla)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
positive_difference = abs(close_tsla_yesterday-day_BY_close_tsla)
# print(positive_difference)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
different_percent = (positive_difference / close_tsla_yesterday)*100
# print(different_percent)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if different_percent > 1:


    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
 parameters_news = {
        "q": "tesla",
        "from": current_day,
        "sortBy": "publishedAt",
        "apiKey": NEWS_APPI_KEY,
    }
    response = requests.get(NEWS_ENDPOINT, params= parameters_news)
    response.raise_for_status()
    data_news = response.json()

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
articles = data_news["articles"]
three_articles = articles[:3]
# print(three_articles)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 
# "Headline:{article title}. \n Brief: {article description}"
formatted_articles = [f"Headline: {article['title']}. \n Brief: {article['description']}" for article in three_articles]

client = Client(TWILIO_SID, TWILIO_ACCOUNT_TOKEN)

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

for article in formatted_articles:
 message = client.messages.create(
     body=article,
     from_="+virtualUsNumber",
     to="personal_number"
 )
#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


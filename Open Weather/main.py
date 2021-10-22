import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

#--------------Constant---------------------
Api_Key = "e636ca19fd209a4991b1c2efb5785d75"
url = "https://api.openweathermap.org/data/2.5/onecall"
lat = 19.088740    #Apatzingan lat = 19.088740 https://www.ventusky.com/?p=19.27;-100.57;7&l=rain-3h you can see where will
                  # be a precipitacion
long = -102.366180 #Apatzingan long = -102.366180
account_sid = "Your account SID"
auth_token = "Your personal Token"

parameters = {
    "lat": lat,
    "lon": long,
    "appid": Api_Key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url, params=parameters)
response.raise_for_status()
data = response.json()

weather_next_condition = []

for hour in range(0,12):

    condition = data["hourly"][hour]["weather"][0]["id"]
    weather_next_condition.append(condition)

if 500 in weather_next_condition:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It is goin to rain. Bring an umbrella.",
        from_='+13253082262',
        to='+523313101164'
    )
    print("it is going to rain, bring an umbrella")
else:
    print("it will be dry")




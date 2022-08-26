import requests
from twilio.rest import Client

api_key = "f646d996ff5fb9cfdefcdc487ef6c24c"

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall?"

account_sid = "AC69949ad9b3aab4747130efce508e697e"
auth_token = "c5be9a1981d19e750a5c7bdc423a99b2"
client = Client(account_sid, auth_token)

weather_params = {
    "lat" : 12.810180,
    "lon":77.591316 ,
    "exclude": {"current","minutely","daily"},
    "appid" : api_key ,
}
response = requests.get(OWM_ENDPOINT,params=weather_params)
response.raise_for_status()

data = response.json()
weather_slice = data["hourly"][:12]
for hour_data in weather_slice:
  condition_code = int(hour_data["weather"][0]["id"])
  if(condition_code < 900):
      will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="BriNG imbrella",
        from_='+19786620913',
        to='+9179828 96684'
    )
    print(message.status)


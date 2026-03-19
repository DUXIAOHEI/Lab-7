import json
import requests

city = 'Moscow'

key = '29e00d7fb526925dc80e18727799e064'

resp= requests.post(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}')
result = json.loads(resp.text)

weather_desc=result["weather"][0]["main"]
humidity=result["main"]["humidity"]
pressure=result["main"]["pressure"]

print("weather:",weather_desc)
print("humidity:",humidity)
print("pressure:",pressure)
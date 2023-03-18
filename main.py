import requests

city = 'Moscow, RU'
appid = "55d3804e5aeb53e5f47f3668bf1a3d4b"
res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()

print('Прогноз погоды на неделю:')

for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nСкорость ветра <", i['wind']['speed'], "> \r\nВидимость <",  i['visibility'],
          "> \r\nТемпература <", '{0:+3.0f}'.format(i['main']['temp']), "> \r\nПогодные условия <", i['weather'][0]['description'],
          ">","\r\n________________________",)

print("")

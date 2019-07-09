import requests
from pprint import pprint
city = input('enter city: ')
url = 'https://samples.openweathermap.org/data/2.5/weather?q=&appid=b6907d289e10d714a6e88b30761fae22'.format(city)


res = requests.get(url)

data = res.json()

temp = data['main']['temp']
wind_speed = data ['wind']['speed']
latitude = data['coord']['lat']
longitude = data['coord']['lon']


description = data['weather'][0]['description']


print('temperature :{} degree celcius '.format( temp))
print('wind speed : ', wind_speed)
print('Lattitude : {}'.format(latitude))
print('longtude : {}'.format(longitude))
print('Description : {}'.format(description))

pprint(res)

pprint(data)






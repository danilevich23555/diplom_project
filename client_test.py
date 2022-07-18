import requests

response = requests.post(
    'http://127.0.0.1:8000/user/login',
    json={ 'email': 'igordolgov@yandex.ru',
          'password': 'wishoting24200956dDv1b2n3z0',})



#
# response = requests.post(
#     'http://127.0.0.1:8000/user/register',
#     json={'first_name': 'Игорь', 'last_name': 'Долгов', 'email': 'igordolgov@yandex.ru',
#           'password': 'wishoting24200956dDv1b2n3z0', 'position': 'референт'})
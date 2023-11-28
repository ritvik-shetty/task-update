import requests

parameters= {
    'page': 1,
    'per_page':2
}

url='https://gorest.co.in/public/v2/users'

response= requests.get(url,params=parameters)

print(response.json())
import requests

BASE="http://127.0.0.1:5000/"

# response=requests.get(BASE)
data=[{"likes":1000, "name":"Python tutorial","views":10000},{"likes":12300, "name":"JS tutorial","views":9910000},
      {"likes":1200, "name":"Html tut","views":12100200},{"likes":90100, "name":"React","views":9910000}]

for i in range(len(data)):
    response=requests.put(BASE+"video/"+str(i),data[i])
    print(response.json())


input()

response= requests.delete(BASE+"video/1")
print(response)


input()


response=requests.get(BASE+"video/2")
print(response.json())


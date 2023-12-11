import requests

header={
    'Accept':'*/*'
}
response= requests.get("http://127.0.0.1:5000/posts", headers=header)

print("Before Update")
list=response.json()
for i in range(len(list)):
    print(list[i])



headerPut={
    'Accept':'*/*',
    'Content-Type': 'application/json'
}

putPayload={
        "address": "Jayanagar",
        "city": "Bangalore",
        "id": 3,
        "name": "Manoj",
        "salary": "65000"
}

responsePut= requests.put("http://127.0.0.1:5000/posts/3",headers=headerPut,json=putPayload)




print("After Update")
response= requests.get("http://127.0.0.1:5000/posts", headers=header)
list=response.json()
for i in range(len(list)):
    print(list[i])


assert responsePut.status_code == 200 , f"expected response to have status code 200 but got {response.status_code}"

print("The program has run successfully and the Status Code is",response.status_code)
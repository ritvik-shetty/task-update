import requests

head={
    'Accept':'text/plain'
}
response= requests.get("https://fakerestapi.azurewebsites.net/api/v1/Authors/13", headers=head)

print("Before Update")
print(response.json())

headerPut={
    'Accept':'text/plain',
    'Content-Type': 'application/json'
}

putPayload={
  "id": 14,
  "idBook": 1111,
  "firstName": "Ritvik",
  "lastName": "Shetty"
}

responsePut= requests.put("https://fakerestapi.azurewebsites.net/api/v1/Authors/13",headers=headerPut,json=putPayload)

print("After Update")
print(responsePut.json())


assert responsePut.status_code == 200 , f"expected response to have status code 200 but got {response.status_code}"

print("The program has run successfully and the Status Code is",response.status_code)
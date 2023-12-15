import requests

header={
    'Accept':'text/plain',
    'Content-Type': 'application/json'
}

request_payload={
  "id": 977710,
  "idBook": 91410,
  "firstName": "Ritvik",
  "lastName": "Shetty"
}

response= requests.post('https://fakerestapi.azurewebsites.net/api/v1/Authors',headers=header,json=request_payload)

print(response.status_code)
print(response.json())

data = response.json()
# print(data['id'])


assert response.status_code == 200 , f"expected response to have status code 200 but got {response.status_code}"

assert data['id'] == 977710 , "There is an error as the ID doesn't match"

print("The ID is",data['id'])
print("The program has run successfully and the Status Code is",response.status_code)

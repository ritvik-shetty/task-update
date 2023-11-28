import requests

head={
    'Accept':'text/plain'
}
response= requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities/7", headers=head)

# print(response.status_code)
# print(response.json())

assert response.status_code==200 , f"expected response to have status code 200 but got {response.status_code}"

print("The program has run successfully and the Status Code is",response.status_code)


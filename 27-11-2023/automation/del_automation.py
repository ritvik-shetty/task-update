import requests

head={
    'Accept':'text/plain'
}

response= requests.get("https://fakerestapi.azurewebsites.net/api/v1/Authors/2", headers=head)
print(response.json())

headDel={
    'Accept': '*/*'
}

responseDel= requests.delete("https://fakerestapi.azurewebsites.net/api/v1/Authors/2",headers=headDel)

print(responseDel.status_code)
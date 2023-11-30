import requests
import json

base_url='https://reqres.in/'

head={'Content-Type':'application/json'}

# payload={
#     "name": "Anil",
#     "job": "lead"
# }

json_file = open('28-11-2023/users.json')

json_payload=json.load(json_file)


response=requests.post(url=base_url+'api/users',headers=head, json=json_payload)

assert response.status_code==201 , f"expected response to have status code 201 but got {response.status_code}"
print(response.text)
print("The program has run successfully and the Status Code is",response.status_code)


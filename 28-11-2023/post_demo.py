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

print(response.status_code)
print(response.text)

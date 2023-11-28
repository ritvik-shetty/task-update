import requests

head = {
    # 'Accept':'*/*',
    'Content-Type':'application/json',
    'Authorization': 'Bearer 15df0d73cae78f084c50be0ed646d33ba55d04525420c4a22b72002583000f9e'
}

body={

    "id": 578276923232992,
    "name": "MohitRj32",
    "email": "Moih=21raj@se23.test",
    "gender": "male",
    "status": "active"
}

url='https://gorest.co.in/public/v2/users'

response= requests.post(url,headers=head,json=body)

print(response.json())
print(response.status_code)
# assert response.status_code == 201

getResponse= requests.get(url+'/'+str( response.json()['id']),headers=head,)
print(getResponse)
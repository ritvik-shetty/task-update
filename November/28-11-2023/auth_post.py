import requests

header = {
    # 'Accept':'*/*',
    'Content-Type':'application/json',
    'Authorization': 'Bearer 15df0d73cae78f084c50be0ed646d33ba55d04525420c4a22b72002583000f9e'
}

body={

    "id": 578276923232992,
    "name": "MohitwewdaRj32",
    "email": "Moh=wearajs@23.t222eest",
    "gender": "male",
    "status": "active"
}

url='https://gorest.co.in/public/v2/users'

response= requests.post(url,headers=header,json=body)

print(response.json())
# print(response.status_code)
# assert response.status_code == 201


assert response.status_code==201 , f"expected response to have status code 201 but got {response.status_code}"

print("The program has run successfully and the Status Code is",response.status_code)


getResponse= requests.get(url+'/'+str( response.json()['id']),headers=header,)
print("GEt Response code is",getResponse)
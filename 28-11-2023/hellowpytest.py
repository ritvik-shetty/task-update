import pytest
import requests

def getrequest_validation():
    header={
        'Content-Type':'application/json'
    }
    
    base_url='https://reqres.in/'

    response=requests.get(url=str(base_url+'api/users/2'),headers=header)
    statuscode= response.status_code
    # print(statuscode)
    return statuscode

    # assert response.status_code == 200 
    # print(response.text)




# def helloworld():
#     return "hello-world"
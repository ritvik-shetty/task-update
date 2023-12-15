import pytest
import requests
from hellowpytest import getrequest_validation

# def test_hello_world():
#     assert helloworld() == "hello-world"


def test_getrequest_validation():
    # header={
    #     'Content-Type':'application/json'
    # }

    # base_url='https://reqres.in/'
     
    assert getrequest_validation() == 200
 
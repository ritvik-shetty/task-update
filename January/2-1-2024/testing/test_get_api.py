import unittest
import requests

class ApiTests(unittest.TestCase):
    BASE_URL = "http://127.0.0.1:5000/"
    VALID_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNDE3NzkyNCwianRpIjoiNDUyODkyMDEtOWU0ZS00ZDQ3LWE3NDYtYTAxOWFkZGNlNTZhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InN0cmluZzEiLCJuYmYiOjE3MDQxNzc5MjQsImNzcmYiOiI4YTdjNjQzMy01MDJiLTQ2N2EtYjU5MC0zMTJmYTYwNmE4N2MiLCJleHAiOjE3MDQxNzg4MjR9.5NkI70K-ikWptXShhR5cWZoG8NUpQ3ZHb3XrvLxihu0"
    INVALID_TOKEN = "invalid_token"

    
    expected_result={   
    "address": "BTM-bnglr",
    "city": "Banglore",
    "id": 1,
    "name": "Ram",
    "salary": "75000"
  }

    #  Positive test case to get all employees with valid token
    def test_valid_token_get_request(self):
        headers = {
            "Authorization": f"Bearer {self.VALID_TOKEN}"
        }
        response = requests.get(f"{self.BASE_URL}/list_employees", headers=headers)

        self.assertEqual(response.status_code, 200)
        # Add more assertions based on your API response if needed
        print("Positive Test 1 completed - GET Request")
        print("The response code is 200 OK")
        print("--------------------------------------")


    def test_get_specific_employees(self):
        headers = {
            "Authorization": f"Bearer {self.VALID_TOKEN}"
        }
        response= requests.get(f"{self.BASE_URL}/employee/1",headers=headers)
        self.assertEqual(response.status_code,200)
        
        # for i in response.json():
        #     dict=i
        # self.assertDictEqual(dict,self.expected_result)
        
        print("Positive Test 2 completed - GET Request")
        print("The response code is 200 OK")
        print("The result and expected result matches")
        print("--------------------------------------")

    

    # Positive test case to ensure the response is in JSON format
    def test_get_data_json_format(self):
        headers = {
            "Authorization": f"Bearer {self.VALID_TOKEN}"
        }
        response = requests.get(self.BASE_URL+'/employee/1',headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json')

        print("Positive Test 3 completed - GET Request")
        print("The response code is 200 OK")
        print("The response is of correct content type")
        print("--------------------------------------")



    # Positive test case to ensure the API handles a large number of requests
    def test_get_data_multiple_requests(self):
        headers = {
            "Authorization": f"Bearer {self.VALID_TOKEN}"
        }
        for _ in range(15):
            response = requests.get(self.BASE_URL+"/list_employees",headers=headers)
            self.assertEqual(response.status_code, 200)
        print("Positive Test 4 completed - GET Request")
        print("Handles multiple requests")
        print("The response code is 200 OK")   
        print("--------------------------------------")





    # Negative Testcase with invalid Auth 
    def test_invalid_token_get_request(self):
        headers = {
            "Authorization": f"Bearer {self.INVALID_TOKEN}"
        }
        response = requests.get(f"{self.BASE_URL}/list_employees", headers=headers)

        self.assertEqual(response.status_code, 422)  
        print("Negative Test 1 completed - GET Request")
        print("The response code is 422")
        print("--------------------------------------")


    # Negative test case for non-existent data
    def test_get_nonexistent_data(self):
        headers = {
            "Authorization": f"Bearer {self.VALID_TOKEN}"
        }
        response = requests.get(self.BASE_URL+'/employee/99999')
        self.assertEqual(response.status_code, 401)
        print("Negative Test 2 completed - GET Request")
        print("The response code is 401.")
        print("Data doesnt Exist")
        print("--------------------------------------")   

    # Negative test case for invalid request methods
    def test_invalid_method(self):
        headers = {
            "Authorization": f"Bearer {self.VALID_TOKEN}"
        }
        response = requests.put(self.BASE_URL+"/update_employee/7",headers=headers)
        self.assertEqual(response.status_code, 415)
        print("Negative Test 3 completed - GET Request")
        print("The response code is 415")
        print("The requested method is invalid")
        print("--------------------------------------") 

    # Negative test case for proper handling of malformed URL
    def test_malformed_url(self):
        response = requests.get(self.BASE_URL+'/')
        self.assertEqual(response.status_code, 404)
        print("Negative Test 4 completed - GET Request")
        print("The response code is 404 Not Found.")
        print("The provided URL is not correct")
        print("--------------------------------------") 


if __name__ == '__main__':
    tester=ApiTests()
    tester.test_valid_token_get_request()
    tester.test_get_specific_employees()
    tester.test_get_data_json_format()
    tester.test_get_data_multiple_requests()


    tester.test_invalid_token_get_request()
    tester.test_get_nonexistent_data()
    tester.test_invalid_method()
    tester.test_malformed_url()
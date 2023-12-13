import unittest
import requests

class TestApi(unittest.TestCase):
    URL="http://127.0.0.1:5000/employee"


    expected_result={
    "address": "Lalbag",
    "city": "Bangalore",
    "id": 1,
    "name": "Raj",
    "salary": "50000"
  }
    # Positive test case to get all employees
    def test_get_all_employees(self):
        response=requests.get(self.URL)
        self.assertEqual(response.status_code,200)
        
        self.assertEqual(len(response.json()),5)
        print("Positive Test 1 completed - GET Request")
        print("The response code is 200 OK")
        print("--------------------------------------")

    # Positive test case to get specific employees
    def test_get_specific_employees(self):
        response= requests.get(self.URL+'/1')
        self.assertEqual(response.status_code,200)
        
        for i in response.json():
            dict=i
        self.assertDictEqual(dict,self.expected_result)
        
        print("Positive Test 2 completed - GET Request")
        print("The response code is 200 OK")
        print("The result and expected result matches")
        print("--------------------------------------")

    # Positive test case to ensure the response contains the expected keys
    def test_get_data_keys(self):
        response = requests.get(self.URL+'/1')
        self.assertEqual(response.status_code, 200)
        
        for i in response.json():
            dict=i
        
        self.assertIn('id', dict)
        self.assertIn('name', dict)
        self.assertIn('address', dict)
        self.assertIn('city', dict)
        self.assertIn('salary', dict)
        
        print("Positive Test 3 completed - GET Request")
        print("The response code is 200 OK")
        print("All keys are present ")
        print("--------------------------------------")

    # Positive test case to ensure the response is in JSON format
    def test_get_data_json_format(self):
        response = requests.get(self.URL+'/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json')

        print("Positive Test 4 completed - GET Request")
        print("The response code is 200 OK")
        print("The response is of correct content type")
        print("--------------------------------------")


    # Positive test case to ensure the API handles a large number of requests
    def test_get_data_multiple_requests(self):
        for _ in range(15):
            response = requests.get(self.URL)
            self.assertEqual(response.status_code, 200)
        print("Positive Test 5 completed - GET Request")
        print("Handles multiple requests")
        print("The response code is 200 OK")   
        print("--------------------------------------")


    # Negative test case for non-existent data
    def test_get_nonexistent_data(self):
        response = requests.get(self.URL+'/99999')
        self.assertEqual(response.status_code, 404)
        print("Negative Test 1 completed - GET Request")
        print("The response code is 404 Not Found.")
        print("Data doesnt Exist")
        print("--------------------------------------")    

    # Negative test case for invalid request methods
    def test_invalid_method(self):
        response = requests.put(self.URL)
        self.assertEqual(response.status_code, 405)
        print("Negative Test 2 completed - GET Request")
        print("The response code is 405 method not allowed.")
        print("The requested method is invalid")
        print("--------------------------------------") 

    # Negative test case for proper handling of malformed URL
    def test_malformed_url(self):
        response = requests.get(self.URL+'/')
        self.assertEqual(response.status_code, 404)
        print("Negative Test 3 completed - GET Request")
        print("The response code is 404 Not Found.")
        print("The provided URL is not correct")
        print("--------------------------------------") 


if __name__ == "__main__":
    tester = TestApi()
    
    tester.test_get_all_employees()
    tester.test_get_specific_employees()
    tester.test_get_data_keys()
    tester.test_get_data_json_format()
    tester.test_get_data_multiple_requests()

    tester.test_get_nonexistent_data()
    tester.test_invalid_method()
    tester.test_malformed_url()
 
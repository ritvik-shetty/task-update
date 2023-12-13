import unittest
import requests

class TestApi(unittest.TestCase):
    URL="http://127.0.0.1:5000/employee"

    data={        
        }

    data1={
       "address": "BTM_LAYOUT",
        "city": "Bangalore",
        "name": "rohit",
        "salary": "49000"
    }

    data2={
        "address": "Jmatar",
        "city": "Jaipur",
        "name": "Pranam",
        "salary": "500320"
    }

    data3={        
        "name": "Raj",
        "salary": "49000"}

    # Positive test case 1: Ensure successful PUT    
    def test_successful_put(self):
        response = requests.put(self.URL+"/1", json=self.data1)
        self.assertEqual(response.status_code, 200)
        print("Positive Test 1 completed - PUT Request")
        print("The response code is 200 OK")
        print("--------------------------------------")


    # Negative test case 1: For non existing data
    def test_unsuccessful_put(self):
        response = requests.put(self.URL+"/9999999", json=self.data1)
        self.assertEqual(response.status_code, 404)
        print("Negative Test 1 completed - PUT Request")
        print("Put for non existing data")
        print("The response code is 404 Not Found")
        print("--------------------------------------")

    # Negative test case 2: For missing parameters
    def test_missing_param(self):
        response = requests.put(self.URL, json=self.data2)
        self.assertEqual(response.status_code, 405)
        print("Negative Test 2 completed - PUT Request")
        print("Passed missing parametes")
        print("The response code is 405 Not allowed")
        print("--------------------------------------")

    # Negative test case 3: For passing empty data
    def test_empty_put(self):
        response = requests.put(self.URL+"/1", json=self.data)
        self.assertEqual(response.status_code, 400)
        print("Negative Test 3 completed - PUT Request")
        print("Passed Empty data")
        print("The response code is 400 BAD REQUEST")
        print("--------------------------------------")

     # Negative test case 4: For passing insufficient data
    def test_insufficient_put(self):
        response = requests.put(self.URL+"/1", json=self.data3)
        self.assertEqual(response.status_code, 400)
        print("Negative Test 4 completed - PUT Request")
        print("passing insufficient data")
        print("The response code is 400 BAD REQUEST")


if __name__ == "__main__":
    tester = TestApi()
    tester.test_successful_put()

    tester.test_unsuccessful_put()
    tester.test_missing_param()
    tester.test_empty_put()
    tester.test_insufficient_put()
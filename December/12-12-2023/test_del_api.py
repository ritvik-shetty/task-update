import unittest
import requests

class TestApi(unittest.TestCase):
    URL="http://127.0.0.1:5000/del_employee"

    # Positive test case to delete an employee
    def test_delete_existing_item(self):
        response=requests.delete(self.URL+'/5')
        self.assertEqual(response.status_code,200)
        
        print("Positive test 1 completed- DELETE Request")
        print("The response code is 200 OK")
        print("-----------------------------------------")


    # Negative test case for non-existent data
    def test_delete_non_existent_item(self):
        response=requests.delete(self.URL+'/999999')
        self.assertEqual(response.status_code,404)
        
        print("Negative test 1 completed- DELETE Request")
        print("The response code is 404 Not Found")
        print("-----------------------------------------")


    # Negative test case for invalid request methods
    def test_invalid_method(self):
        response = requests.put(self.URL)
        self.assertEqual(response.status_code, 404)
        print("Negative Test 2 completed - DELETE Request")
        print("The response code is 404 ")
        print("The requested method is invalid")
        print("--------------------------------------") 

    # Negative test case for proper handling of malformed URL
    def test_malformed_url(self):
        response = requests.delete(self.URL+'/malformed')
        self.assertEqual(response.status_code, 404)
        print("Negative Test 3 completed - DELETE Request")
        print("The response code is 404 Not Found.")
        print("The provided URL is not correct")
        print("--------------------------------------") 


if __name__ == "__main__":
    tester = TestApi()
    # tester.test_delete_existing_item()

    tester.test_delete_non_existent_item()
    tester.test_invalid_method()
    tester.test_malformed_url()
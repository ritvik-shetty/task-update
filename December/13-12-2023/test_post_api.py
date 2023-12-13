import unittest
import requests

class TestApi(unittest.TestCase):
    URL="http://127.0.0.1:5000/employee"

    data={
        "name": "Karthik",
        "address": "kundapura-street",
        "city": "udupi",
        "salary": "97765"
    }

    # Positive test case 1: Ensure successful creation of data
    def test_create_data_successful(self):
        response = requests.post(self.URL, json=self.data)
        self.assertEqual(response.status_code,201)
        print("Positive Test 1 completed - POST Request")
        print("The response code is 201 OK")
        
    # Positive test case 2: Ensure successful creation with additional optional fields
    def test_create_data_with_optional_fields(self):
        data_to_post = {'name': 'Optional Data', "address": "optional address","city": "optional city","salary": "optional salary" ,"description": "Additional Info"}
        response = requests.post(self.URL, json=data_to_post)
        self.assertEqual(response.status_code,201)
        print("Positive Test 2 completed - POST Request")
        print("The response code is 201 OK")

    
    # Positive test case 3: Ensure successful creation with special characters
    def test_create_data_with_special_characters(self):
        data_to_post = {"name": "Special Characters !@#$%^&*()","address": "kundapura-street","city": "udupi","salary": "97765"}
        response = requests.post(self.URL, json=data_to_post)
        self.assertEqual(response.status_code,201)
        print("Positive Test 3 completed - POST Request")
        print("The response code is 201 OK")

    # Positive test case 4: Ensure proper handling of duplicate data
    def test_create_duplicate_data(self):
        data_to_post = {"name": "Karthik",
        "address": "kundapura-street",
        "city": "udupi",
        "salary": "97765"}
        response1 = requests.post(self.URL, json=data_to_post)
        response2 = requests.post(self.URL, json=data_to_post)

        self.assertEqual(response1.status_code, 201)
        print("Positive Test 4 completed - POST Request")
        print("1st POST Request")
        print("The response code is 201 OK")
        self.assertEqual(response2.status_code, 201)
        print("2nd POST request with same data(But id will change)")
        print("The response code is 201 OK")



    # Negative test case 1: Missing attributes 
    def test_field_missing(self):
        data_to_post = {"name": "Karthik","city": "udupi","salary": "97765"}
        response = requests.post(self.URL, json=data_to_post)
        self.assertEqual(response.status_code,400)
        print("Negative Test 1 completed - POST Request")
        print("The response code is 400 error")
        print("Since fields are missing")

    # Negative test case 2: Missing values 
    def test_data_missing(self):
        data_to_post = {"name": "Karthik","city": "udupi", "address": "kundapura-street", "salary": ""}
        response = requests.post(self.URL, json=data_to_post)
        self.assertEqual(response.status_code,400)
        print("Negative Test 2 completed - POST Request")
        print("The response code is 400 error")
        print("Since data in field missing")

    # Negative test case 3: Incorrect attribute name
    def test_attr_name_error(self):
        data_to_post = {"name": "Karthik","city": "udupi", "address": "kundapura-street", "sal": "99845"}
        response = requests.post(self.URL, json=data_to_post)
        self.assertEqual(response.status_code,400)
        print("Negative Test 3 completed - POST Request")
        print("The response code is 400 error")
        print("Since data in field missing")

    

if __name__ == "__main__":
    tester = TestApi()
    # tester.test_create_data_successful()
    # tester.test_create_data_with_optional_fields()
    # tester.test_create_data_with_special_characters()
    # tester.test_create_duplicate_data()
    # tester.test_field_missing()
    # tester.test_data_missing()
    tester.test_attr_name_error()
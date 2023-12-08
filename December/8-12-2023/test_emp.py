import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp_1=Employee('Carl','Jeff',45000)
        self.emp_2=Employee('Robert','Smith',60000)
    
    def test_email(self):
        self.assertEqual(self.emp_1.email,'Carl.Jeff@email.com')
        print("test case 1 - for email - successful")
        self.assertEqual(self.emp_2.email,'Robert.Smith@email.com')
        print("test case 2 - for email - successful")
        

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname,'Carl Jeff')
        print("test case 1 - for fullname - successful")
        self.assertEqual(self.emp_2.fullname,'Robert Smith')
        print("test case 2 - for fullname - successful")

    def test_apply_raise(self):

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay,47250)
        print("test case 1 - for apply rise - successful")
        self.assertEqual(self.emp_2.pay,63000)
        print("test case 2 - for apply rise - successful")

if __name__=='__main__':
    unittest.main()
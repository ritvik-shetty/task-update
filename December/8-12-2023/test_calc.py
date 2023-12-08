import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        
        self.assertEqual(calc.add(10,5),15)
        print("test case 1 - for add - successful")
        self.assertEqual(calc.add(-1,1),0)
        print("test case 2 - for add - successful")
        self.assertEqual(calc.add(-1,-1),-2)
        print("test case 3 - for add - successful")

    def test_subtract(self):
        
        self.assertEqual(calc.subtract(10,5),5)
        print("test case 1 - for sub - successful")
        self.assertEqual(calc.subtract(-1,1),-2)
        print("test case 2 - for sub - successful")
        self.assertEqual(calc.subtract(-1,-1),0)
        print("test case 3 - for sub - successful")

    def test_mult(self):
        
        self.assertEqual(calc.multiply(10,5),50)
        print("test case 1 - for mul - successful")
        self.assertEqual(calc.multiply(-1,1),-1)
        print("test case 2 - for mul - successful")
        self.assertEqual(calc.multiply(-1,-1),1)
        print("test case 3 - for mul - successful")


    def test_div(self):
        
        self.assertEqual(calc.divide(10,5),2)
        print("test case 1 - for div - successful")

        self.assertEqual(calc.divide(-1,1),-1)
        print("test case 2 - for div - successful")

        self.assertEqual(calc.divide(-1,-1),1)
        print("test case 3 - for div - successful")
    

        # self.assertRaises(ValueError,calc.divide,10,0)
        with self.assertRaises(ValueError):
            calc.divide(10,0)
            


if __name__=='__main__':
    unittest.main()
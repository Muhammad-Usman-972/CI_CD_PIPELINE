from main import add , sub , mul , div
import unittest

class Test(unittest.TestCase):

        def test_add(self):
            self.assertEqual(add(10,20),30)
            
        def test_sub(self):
            self.assertEqual(sub(20,10),10)

        def test_mul(self):
            self.assertEqual(mul(10,20),200)
        
        def test_div(self):
            self.assertEqual(div(20,10),2)
            self.assertEqual(div(20,0),None)

if __name__ == "__main__":
    unittest.main()
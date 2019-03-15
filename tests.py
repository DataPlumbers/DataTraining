import unittest

import driver as dr

class Test_ML_Component(unittest.TestCase):

    def test_driver_classify_usage(self):
        self.assertRaises(ValueError, dr.classify, ("data", "data"), [])
        self.assertRaises(ValueError, dr.classify, ("data"), ["file"])

    def test_driver_classify_fnf(self):
        self.assertRaises(FileNotFoundError, dr.classify, ("data", "data"), ["file"])
        self.assertRaises(FileNotFoundError, dr.classify, ("data", "data"), ["file.csv"])
        self.assertRaises(FileNotFoundError, dr.classify, ("data", "data"),
                          ["file.json"])

if __name__ == '__main__':
    unittest.main()

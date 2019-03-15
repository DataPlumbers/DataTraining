import unittest

import driver as dr
import entity as ent
class Test_ML_Component(unittest.TestCase):

    def test_driver_classify_usage(self):
        print("Testing Driver.classify parameter checks...")
        self.assertRaises(ValueError, dr.classify, ("data", "data"), [])
        self.assertRaises(ValueError, dr.classify, ("data"), ["file"])

    def test_driver_classify_fnf(self):
        print("Testing Driver.classify with bad filepaths...")
        self.assertRaises(FileNotFoundError, dr.classify, ("data", "data"), ["file"])
        self.assertRaises(FileNotFoundError, dr.classify, ("data", "data"), ["file.csv"])
        self.assertRaises(FileNotFoundError, dr.classify, ("data", "data"),
                          ["file.json"])

    def test_entity_get_entities_file(self):
        print("Testing Entity.get_entities_file on small dataset...")
        entities = ent.get_entities_file("datasets/small.csv")
        self.assertTrue(isinstance(entities, dict))
        self.assertNotEqual(0, len(entities))

if __name__ == '__main__':
    unittest.main()

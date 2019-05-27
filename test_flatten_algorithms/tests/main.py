import unittest
from .flatten_funcs import TestFlattenFunctions
from .data_generation import TestGenerationData

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestFlattenFunctions())
    suite.addTest(TestGenerationData())
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
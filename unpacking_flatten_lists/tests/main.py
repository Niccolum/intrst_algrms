import unittest
from unpacking_flatten_lists.tests.flatten_funcs import (
    TestFlattenFunctions,
    TestProfileFlattenFunctions)
from unpacking_flatten_lists.tests.data_generation import TestGenerationData


def main():
    suite = unittest.TestSuite()
    suite.addTest(TestGenerationData())
    suite.addTest(TestFlattenFunctions())
    suite.addTest(TestProfileFlattenFunctions())
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(main())

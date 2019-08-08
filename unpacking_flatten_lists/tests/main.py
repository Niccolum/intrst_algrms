import unittest
from .flatten_funcs import TestFlattenFunctions
from .data_generation import TestGenerationData


def main():
    suite = unittest.TestSuite()
    suite.addTest(TestGenerationData())
    suite.addTest(TestFlattenFunctions())
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(main())

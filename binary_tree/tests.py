import unittest
import types

from funcs import SingleNodeClass, TwoNodeClass
from data import min_datalist, middle_datalist, big_datalist


class TestNodes(unittest.TestCase):

    data = [min_datalist, middle_datalist, big_datalist]

    def tree_testing(self, instance, datalist):
        for i in datalist:
            instance.add_node(i)
        result = instance.tree_data()
        if isinstance(result, types.GeneratorType):
            result = list(result)
        self.assertEqual(result, sorted(datalist))

    def test_data_SingleNodeClass(self):
        for datalist in self.data:
            node = SingleNodeClass()
            self.tree_testing(node, datalist)

    def test_data_TwoNodeClass(self):
        for datalist in self.data:
            node = TwoNodeClass()
            self.tree_testing(node, datalist)
            

if __name__ == '__main__':
    unittest.main()

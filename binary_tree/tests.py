import unittest
from typing import List
from numbers import Integral

from binary_tree.funcs import BisectNodeClass, SingleNodeClass, TwoNodeClass, BaseNodeClass
from binary_tree.data import datalist_100, datalist_1000, datalist_10000, datalist_100000, datalist_1000000


class TestNodes(unittest.TestCase):
    data = [datalist_100, datalist_1000, datalist_10000, datalist_100000, datalist_1000000]

    def tree_testing(self, instance: BaseNodeClass, datalist: List[Integral]):
        for i in datalist:
            instance.add_node(i)
        result = list(instance.tree_data())
        self.assertEqual(result, sorted(datalist))

    def test_data_SingleNodeClass(self):
        for datalist in self.data:
            node = SingleNodeClass()
            self.tree_testing(node, datalist)

    def test_data_TwoNodeClass(self):
        for datalist in self.data:
            node = TwoNodeClass()
            self.tree_testing(node, datalist)

    def test_data_BisectNodeClass(self):
        for datalist in self.data:
            node = BisectNodeClass()
            self.tree_testing(node, datalist)


if __name__ == '__main__':
    unittest.main()

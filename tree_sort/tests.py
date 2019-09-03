import unittest
from typing import List
from numbers import Integral

from tree_sort.funcs import (
    BisectNodeClass,
    SingleNodeClass,
    TwoNodeClass,
    BaseNodeClass,
    profile)

from tree_sort.data import datalist_100, datalist_1000, datalist_10000


class TestNodes(unittest.TestCase):
    data = [datalist_100, datalist_1000, datalist_10000]

    def tree_testing(self, instance: BaseNodeClass, datalist: List[Integral]) -> None:
        for i in datalist:
            instance.add_node(i)
        result = list(instance.tree_data())
        self.assertEqual(result, sorted(datalist))

    def test_data_SingleNodeClass(self) -> None:
        for datalist in self.data:
            node = SingleNodeClass()
            self.tree_testing(node, datalist)

    def test_data_TwoNodeClass(self) -> None:
        for datalist in self.data:
            node = TwoNodeClass()
            self.tree_testing(node, datalist)

    def test_data_BisectNodeClass(self) -> None:
        for datalist in self.data:
            node = BisectNodeClass()
            self.tree_testing(node, datalist)

    def test_profile(self) -> None:
        # check for func done
        self.assertEqual(profile(), None)


if __name__ == '__main__':
    unittest.main()

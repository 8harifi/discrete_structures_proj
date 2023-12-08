import unittest
from main import (
    numofpath_func,
    check_hamilton_availability,
    shortestpath_func,
    euler_func
)


class TestCalculator(unittest.TestCase):
    def test_numofpath(self):
        paths = {
            'Isfahan': {'Tehran': 200, 'Yazd': 500},
            'Kerman': {'Yazd': 300},
            'Tehran': {'Isfahan': 200, 'Yazd': 100},
            'Yazd': {'Isfahan': 500, 'Kerman': 300, 'Tehran': 100}
        }
        src = "Isfahan"
        dst = "Yazd"
        res = numofpath_func(src, dst, paths)
        self.assertEqual(res, 2)


if __name__ == "__main__":
    unittest.main()

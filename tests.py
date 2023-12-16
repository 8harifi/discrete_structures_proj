import unittest

from icecream import ic

from main import (
    numofpath_func,
    check_hamilton_availability,
    shortestpath_func,
    euler_func
)


class TestCalculator(unittest.TestCase):
    def test_numofpath_1(self):
        paths = {
            'Isfahan': {'Tehran': 200, 'Yazd': 500},
            'Kerman': {'Yazd': 300},
            'Tehran': {'Isfahan': 200, 'Yazd': 100},
            'Yazd': {'Isfahan': 500, 'Kerman': 300, 'Tehran': 100}
        }
        src = "Kerman"
        dst = "Isfahan"
        res = numofpath_func(src, dst, paths)
        self.assertEqual(res, 2)

    def test_numofpath_2(self):
        paths = {
            'Kerman': {'Yazd': 300},
            'Yazd': {'Kerman': 300, 'Tehran': 100, 'Isfahan': 500},
            'Tehran': {'Yazd': 100, 'Isfahan': 200},
            'Isfahan': {'Yazd': 500, 'Tehran': 200}
        }
        src = "Kerman"
        dst = "Isfahan"
        res = numofpath_func(src, dst, paths)
        self.assertEqual(res, 2)

    def test_euler_1(self):
        paths = {
            'Kerman': {'Yazd': 300},
            'Yazd': {'Kerman': 300, 'Tehran': 100, 'Isfahan': 500},
            'Tehran': {'Yazd': 100, 'Isfahan': 200},
            'Isfahan': {'Yazd': 500, 'Tehran': 200}
        }
        is_circuit, res = euler_func(paths)
        self.assertEqual(is_circuit, False)
        self.assertEqual(
            res,
            [
                {'Yazd', 'Kerman'},
                {'Tehran', 'Yazd'},
                {'Tehran', 'Isfahan'},
                {'Isfahan', 'Yazd'}
            ]
        )

    def test_shortestpath_1(self):
        paths = {
            'Kerman': {'Yazd': 300},
            'Yazd': {'Kerman': 300, 'Tehran': 100, 'Isfahan': 500},
            'Tehran': {'Yazd': 100, 'Isfahan': 200},
            'Isfahan': {'Yazd': 500, 'Tehran': 200}
        }
        res, weight = shortestpath_func("Kerman", "Isfahan", paths)
        self.assertEqual(res, "Kerman Yazd Tehran Isfahan")
        self.assertEqual(weight, 300 + 100 + 200)

    def test_shortestpath_2(self):
        paths = {
            'Kerman': {'Yazd': 300},
            'Yazd': {'Kerman': 300, 'Tehran': 100, 'Isfahan': 500},
            'Tehran': {'Yazd': 100, 'Isfahan': 200},
            'Isfahan': {'Yazd': 500, 'Tehran': 200}
        }
        res, weight = shortestpath_func("Yazd", "Isfahan", paths)
        self.assertEqual(res, "Yazd Tehran Isfahan")
        self.assertEqual(weight, 100 + 200)

    def test_shortestpath_3(self):
        paths = {
            'Kerman': {'Yazd': 300},
            'Yazd': {'Kerman': 300, 'Tehran': 100, 'Isfahan': 500},
            'Tehran': {'Yazd': 100, 'Isfahan': 200},
            'Isfahan': {'Yazd': 500, 'Tehran': 200}
        }
        res, weight = shortestpath_func("Yazd", "Tehran", paths)
        self.assertEqual(res, "Yazd Tehran")
        self.assertEqual(weight, 100)


if __name__ == "__main__":
    unittest.main()

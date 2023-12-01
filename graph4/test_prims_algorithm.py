# test_prim_algorithm.py
import unittest
from prims_algorithm import prim_algorithm

class TestPrimAlgorithm(unittest.TestCase):
    def test_prim_algorithm(self):
        graph = [
            [0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]
        ]

        expected_result = [(0, 1), (1, 2), (1, 4), (0, 3)]
        self.assertEqual(prim_algorithm(graph), expected_result)

if __name__ == '__main__':
    unittest.main()

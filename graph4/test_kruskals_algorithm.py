import unittest
from kruskals_algorithm import kruskal_algorithm

class TestKruskalAlgorithm(unittest.TestCase):
    def test_kruskal_algorithm(self):
        edges = [(13, 0, 1), (18, 0, 2), (17, 0, 3), (14, 0, 4), (22, 0, 5), (22, 1, 4),
                 (26, 1, 2), (3, 2, 3), (19, 3, 5)]
        n = 6

        expected_result = edges = [(3, 2, 3), (13, 0, 1), (14, 0, 4), (17, 0, 3), (19, 3, 5)]



        self.assertEqual(kruskal_algorithm(edges, n), expected_result)

if __name__ == '__main__':
    unittest.main()

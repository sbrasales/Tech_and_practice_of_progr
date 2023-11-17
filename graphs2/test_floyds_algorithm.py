import unittest
import math

from floyds_algorithm import get_path, W

N = len(W)
P = [[v for v in range(N)] for u in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            d = W[i][k] + W[k][j]
            if W[i][j] > d:
                W[i][j] = d
                P[i][j] = k

class TesYourCod(unittest.TestCase):

    def test_get_path(self):
        self.assertEqual(get_path(P, 4, 1), [4, 1])
        self.assertEqual(get_path(P, 3, 2), [3, 2])

if __name__ == '__main__':
    unittest.main()




import unittest
from Knuth_Morris_Pratt import compute_lps_array, kmp_search

class TestKMP(unittest.TestCase):

    def test_lps_array(self):
        self.assertEqual(compute_lps_array("ABABAC"), [0, 0, 1, 2, 3, 0])
        self.assertEqual(compute_lps_array("AAAA"), [0, 1, 2, 3])
        self.assertEqual(compute_lps_array("ABCDE"), [0, 0, 0, 0, 0])
        self.assertEqual(compute_lps_array("AABAACAABAA"), [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5])

    def test_kmp_search(self):
        text = "ABABDABACDABABCABAB"
        pattern = "ABABCABAB"
        self.assertEqual(kmp_search(text, pattern), [10])

        text = "AAAAABAAABA"
        pattern = "AAAA"
        self.assertEqual(kmp_search(text, pattern), [0, 1])

if __name__ == '__main__':
    unittest.main()


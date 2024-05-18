import unittest
from Boyer_Moore import last_occurrence, boyer_moore_match

class TestBoyerMoore(unittest.TestCase):

    def test_last_occurrence(self):
        pattern = "ABABAC"
        alphabet = set("ABC")
        last = last_occurrence(pattern, alphabet)
        self.assertEqual(last('A'), 4)
        self.assertEqual(last('B'), 3)
        self.assertEqual(last('C'), 5)
        self.assertEqual(last('D'), -1)  # D is not in the pattern

    def test_boyer_moore_match(self):
        text = "ABABDABACDABABCABAB"
        pattern = "ABABCABAB"
        self.assertEqual(boyer_moore_match(text, pattern), 10)

        text = "hello world"
        pattern = "world"
        self.assertEqual(boyer_moore_match(text, pattern), 6)

if __name__ == '__main__':
    unittest.main()

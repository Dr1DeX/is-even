from main import is_even, is_even_mod
import unittest


class TestCorrectRun(unittest.TestCase):
    def test_is_even(self):
        corner_case = [
            (2, True),
            (4, True),
            (0, True),
            (3, False),
        ]

        for params, expected in corner_case:
            with self.subTest(params=params, expected=expected):
                actual = is_even(params)
                actual_mod = is_even_mod(params)
                self.assertEqual(actual, expected)
                self.assertEqual(actual_mod, expected)


if __name__ == '__main__':
    unittest.main()

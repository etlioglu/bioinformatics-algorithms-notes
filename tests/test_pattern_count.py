""" unittest example """

import unittest

from count_pattern import count_pattern


class PatternCount(unittest.TestCase):
    def test_pattern_count_simple_case(self):
        text = "GCGCG"
        pattern = "GCG"
        result = count_pattern(text, pattern)
        self.assertEqual(result, 2)

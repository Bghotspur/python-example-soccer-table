#! /usr/bin/python
import unittest
from solution import *


class MatchResultMock(object):

    def __init__(self, teams, scores):
        self.teams = teams
        self.scores = scores


class TestMatchResult(unittest.TestCase):

    def test___init__(self):
        """Test that we correctly parse result input lines"""
        m = MatchResult(""" team A with spaces 1, Snakes 3
""")
        self.assertTupleEqual(m.teams, ('team A with spaces', 'Snakes'))
        self.assertTupleEqual(m.scores, (1, 3))


class TestTable(unittest.TestCase):

    def test_record_result(self):
        """Test that table dictionary is updated with correct teams and points.

        3 points for a win, 0 for loss, 1 for tie."""
        t = Table()
        # test tie
        t.record_result(MatchResultMock(('a', 'b'), (0, 0)))
        self.assertDictEqual({'a': 1, 'b': 1}, t.teams)
        # test loss for existing team, win for new team
        t.record_result(MatchResultMock(('a', 'c'), (50, 100)))
        self.assertDictEqual({'a': 1, 'b': 1, 'c': 3}, t.teams)
        # test win for existing team, loss for new team
        t.record_result(MatchResultMock(('a', 'd'), (4, 0)))
        self.assertDictEqual({'a': 4, 'b': 1, 'c': 3, 'd': 0}, t.teams)

    def test_generate_rankings(self):
        """Test that our ranking output lines are generated and formatted correctly"""
        input = """Manchester United 3, Chelsea 3
Swansea City 0, Liverpool 2
Aston Villa 1, Arsenal 2
Chelsea 2, QPR 0"""
        expected_output = """1. Chelsea, 4 pts
2. Arsenal, 3 pts
2. Liverpool, 3 pts
4. Manchester United, 1 pt
5. Aston Villa, 0 pts
5. QPR, 0 pts
5. Swansea City, 0 pts
"""
        t = Table()
        for line in input.splitlines(True):
            t.record_result(MatchResult(line))
        output = ""
        for line in t.generate_rankings():
            output += line + "\n"
        self.assertMultiLineEqual(expected_output, output)

    def test__rank_comparison(self):
        """Test that _rank_comparison correctly sorts by points and alphabet."""
        t = Table()
        # start in unsorted order
        t.teams = {"a": 2, "cxx": 5,  "bstring": 5}
        self.assertListEqual(sorted(t.teams, cmp=t._rank_comparison),
                             ['bstring', 'cxx', 'a'])


if __name__ == '__main__':
    unittest.main()

"""
An example of a basic unit test, and test cases
that use the `unittest.TestCase` class.
"""

from unittest import TestCase

import insight


def test_insight_instantiates():
    # A smoke test
    obj = insight.InsightObject()
    assert obj


class InsightObjectTestCase(TestCase):
    def setUp(self):
        # this is always ran before each test on this object
        self.Iobj = insight.InsightObject()

    def tearDown(self):
        # this is always ran after each test on this object
        pass

    def test_fizz(self):
        assert self.Iobj.fizz() == "buzz"

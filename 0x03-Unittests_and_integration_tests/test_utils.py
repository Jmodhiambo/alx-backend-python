#!/usr/bin/env python3
"""
Unittesting
"""

import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Testing class for the utils.py"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])


    def test_access_nested_map(self, nested_map, path, expected):
        """Tests access_nested_map() from util.py"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

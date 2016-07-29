#!/usr/bin/env python
"""Unit tests for the project1.authentcation module."""


from unittest import TestCase
from mock import patch
import day1.unittesting.project.simple as spl

# this test will fail
class StandAloneTests(TestCase):
    """Test the stand-alone module functions."""

    @patch('__builtin__.open')
    def test_count(self, mock_open):
        """Test the count function."""
        self.assertTrue(spl.count() == 20)

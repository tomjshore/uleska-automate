from unittest import TestCase
import re
from uleskaautomate import get_version


class UleskaAutomateTest(TestCase):
    def test_get_version_returns_sequence_base_version(self):
        # given
        expected_format = r"\d*\.\d*\.\d*"
        # when
        version = get_version()

        # then
        self.assertRegex(version, expected_format)
        self.assertEqual(1, 1)

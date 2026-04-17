from django.test import TestCase

class BasicTest(TestCase):
    def test_sanity(self):
        self.assertEqual(1, 1)
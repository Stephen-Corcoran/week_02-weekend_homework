import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest1 = Guest("Stephen")

    def test_guest_has_name(self):
        self.assertEqual("Stephen", self.guest1.name)
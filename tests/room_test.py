import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("Room 1")
        self.guest1 = Guest("Stephen")
        
    def test_room_has_name(self):
        self.assertEqual("Room 1", self.room1.name)

    def test_room_starts_empty(self):
        self.assertEqual(0, len(self.room1.guest_list))

    def test_playlist_starts_empty(self):
        self.assertEqual(0, len(self.room1.playlist))

    def test_check_in_guest(self):
        self.room1.check_in_guest(self.guest1)
        self.assertEqual(1, len(self.room1.guest_list))

    def test_check_out_guest(self):
        self.room1.check_in_guest(self.guest1)
        self.room1.check_out_guest(self.guest1)
        self.assertEqual(0, len(self.room1.guest_list))

    def test_add_song_to_playlist(self):
        self.song1 = Song("WAP", 4.12, "Cardi B feat. Megan Thee Stallion")
        self.room1.add_song_to_playlist(self.song1)
        self.assertEqual(1, len(self.room1.playlist))
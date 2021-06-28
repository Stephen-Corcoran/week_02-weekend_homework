import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("WAP", 4.12, "Cardi B feat. Megan Thee Stallion")

    def test_song_has_title(self):
        self.assertEqual("WAP", self.song1.title)

    def test_song_has_duration(self):
        self.assertEqual(4.12, self.song1.duration)

    def test_song_has_artist(self):
        self.assertEqual("Cardi B feat. Megan Thee Stallion", self.song1.artist)
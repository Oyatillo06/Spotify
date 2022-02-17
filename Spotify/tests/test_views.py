from unittest import TestCase

from django.test import Client
from musicapp.models import Artis,Album
from musicapp.serializers import AlbumSerializer,SongSerializer,ArtisSerializer

class TestArtistViewSet(TestCase):
    def setUp(self) -> None:
        self.cl=Client()
    def test_get_artists(self):
        natija=self.cl.get("/artis/2/")
        print(natija)
        assert natija.status_code==200
class TestSongViewSet(TestCase):
    def setUp(self) -> None:
        self.cl=Client()
    def test_get_songs(self):
        natija=self.cl.get("/song/")
        print(natija)
        assert natija.status_code==200





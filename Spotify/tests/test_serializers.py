from unittest import TestCase
from musicapp.models import Artis,Album
from musicapp.serializers import AlbumSerializer,SongSerializer,ArtisSerializer
class TestArtistSer(TestCase):
    def setUp(self) -> None:
        pass
    def test_yes_valid(self):
        artist={
            "id":1,
            "name":"Lee",
            "yonalish":"Kpop",
            "description":"Xitoy lik "


        }
        ser=ArtisSerializer(data=artist)
        assert ser.is_valid()==False
        assert ser.errors['name'][0]=="Bunaqa ashulachi yoq"
    def test_validate(self):
        artist = {
            "id": 1,
            "name": "Leee",
            "yonalish": "Kpop",
            "description": "Xitoy lik "

        }
        ser = ArtisSerializer(data=artist)
        assert ser.is_valid() == True
    def test_valid(self):
        artist={
            "id":1,
            "name":"Lee",
            "yonalish":"Kpop",
            "image":"https://www.sadsas.png",
            "description":"Xitoy lik "


        }
        ser=ArtisSerializer(data=artist)
        assert ser.is_valid()==False
        # assert ser.errors['image']=="Bunday rasm formati yoq"







    def test_artist(self):
        a=Artis.objects.all()
        malumot=ArtisSerializer(a,many=True)
        assert malumot.data[0]["id"]==1
        self.assertTrue(malumot.data[0]["id"]==1)
        self.assertEqual(malumot.data[0]["id"],1)
        # assert malumot.data[0]["name"]=="Ozodbek Nazarbekov"
        # assert malumot.data[0]["yonalish"] == "Klassika"
    def test_name_validation(self):
        a1=Artis.objects.get(id=1)
        a1.name="Le"
        malumot=ArtisSerializer(a1)
        assert  malumot.data["name"]=="Le"


class TestAlbumSer(TestCase):
    def test_album(self):
        a1 = Album.objects.all()
        malumot = AlbumSerializer(a1, many=True)
        assert malumot.data[0]["title"] == "sadsadsafsad"
        assert malumot.data[0]["date"] == "2016-10-12"
        assert malumot.data[0]["artist"] == 1














from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from .models import Artis,Album,Song

class ArtisSerializer(ModelSerializer):
    class Meta:
        model=Artis
        fields=["id","name","yonalish","description","image"]
    def validate_name(self,qiymat):
        if len(qiymat)<=3:
            raise ValidationError("Bunaqa ashulachi yoq")
        return qiymat

    def validate_image(self, qiymat):
        if not qiymat.endswith(".png"):
            raise ValidationError(detail="Bunday rasm formati yoq")
        return qiymat
   
class AlbumSerializer(ModelSerializer):
    class Meta:
        model=Album
        fields=["id","title","date","cover","artist"]
class SongSerializer(ModelSerializer):
    class Meta:
        model=Song
        fields=["id","title","cover","lyrics","duration","sourse","albom"]

    def validate_source(self, qiymat):
        if not qiymat.endswith(".mp3"):
            raise ValidationError(detail="Bunday uzun sarlavha bolishi mumkin emas")
        return qiymat
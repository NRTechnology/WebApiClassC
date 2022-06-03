from rest_framework import serializers

from .models import Mahasiswa


class MahasiswaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mahasiswa
        fields = ['Nim', 'Nama', 'TmpLahir', 'TglLahir', 'Alamat', 'Kelamin']

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import Mahasiswa
from .serializer import MahasiswaSerializer


class MahasiswaViewSet(viewsets.ModelViewSet):
    queryset = Mahasiswa.objects.all()
    serializer_class = MahasiswaSerializer

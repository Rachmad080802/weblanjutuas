from rest_framework import viewsets
from .models import Siswa, Kelas, Absensi
from .serializers import SiswaSerializer, KelasSerializer, AbsensiSerializer

class KelasViewSet(viewsets.ModelViewSet):
    queryset = Kelas.objects.all()
    serializer_class = KelasSerializer
    
class SiswaViewSet(viewsets.ModelViewSet):
    queryset = Siswa.objects.all()
    serializer_class = SiswaSerializer

class AbsensiViewSet(viewsets.ModelViewSet):
    queryset = Absensi.objects.all()
    serializer_class = AbsensiSerializer

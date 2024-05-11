from rest_framework import serializers
from .models import Siswa, Kelas, Absensi

class SiswaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Siswa
        fields = '__all__'

class KelasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kelas
        fields = '__all__'

class AbsensiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Absensi
        fields = '__all__'

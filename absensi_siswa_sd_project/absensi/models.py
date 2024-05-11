from django.db import models

class Kelas(models.Model):
    nama = models.CharField(max_length=100)
    guru_pengajar = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nama

class Siswa(models.Model):
    nama = models.CharField(max_length=100)
    kelas = models.ForeignKey(Kelas, on_delete=models.CASCADE)
    nomor_absen = models.PositiveIntegerField()
    
    def __str__(self):
        return self.nama

class Absensi(models.Model):
    siswa = models.ForeignKey(Siswa, on_delete=models.CASCADE)
    tanggal = models.DateField()
    hadir = models.BooleanField()
    
    def __str__(self):
        return f"{self.siswa.nama} - {self.tanggal}"

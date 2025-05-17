from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import hashlib

class Tugas(models.Model):
    mahasiswa = models.ForeignKey(User, on_delete=models.CASCADE)
    file_tugas = models.FileField(upload_to='tugas/')
    timestamp = models.DateTimeField(auto_now_add=True)
    hash_tugas = models.CharField(max_length=64)
    previous_hash = models.CharField(max_length=64)
    grades_tugas = models.TextField(null=True, blank=True)

    def calculate_hash(self):
        data = f"{self.mahasiswa.id}{self.file_tugas.name}{self.timestamp}{self.previous_hash}"
        return hashlib.sha256(data.encode()).hexdigest()

    def save(self, *args, **kwargs):
        if not self.hash_tugas:
            self.hash_tugas = self.calculate_hash()
        super().save(*args, **kwargs)

class Nilai(models.Model):
    tugas = models.OneToOneField(Tugas, on_delete=models.CASCADE)
    nilai_terenkripsi = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    signature = models.TextField()
    hash_nilai = models.CharField(max_length=64)
    nilai_asli = models.IntegerField(null=True, blank=True)
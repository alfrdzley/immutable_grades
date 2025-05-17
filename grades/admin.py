from django.contrib import admin

# Register your models here.
from .models import Tugas, Nilai

admin.site.register(Tugas)
admin.site.register(Nilai)
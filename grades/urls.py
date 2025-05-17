from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_tugas, name='upload_tugas'),
    path('nilai/<int:tugas_id>/', views.input_nilai, name='input_nilai'),
    path('verifikasi/<int:nilai_id>/', views.verifikasi_nilai, name='verifikasi_nilai'),
    path('list/', views.list_tugas, name='list_tugas'),
]
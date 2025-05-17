from django import forms
from .models import Tugas, Nilai

class TugasForm(forms.ModelForm):
    class Meta:
        model = Tugas
        fields = ['file_tugas']

class NilaiForm(forms.ModelForm):
    nilai_asli = forms.IntegerField(min_value=0, max_value=100)
    class Meta:
        model = Nilai
        fields = ['nilai_asli']
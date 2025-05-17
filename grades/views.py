from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Tugas, Nilai
from .forms import TugasForm, NilaiForm
from .utils import load_keys, encrypt_nilai, verify_signature


@login_required
def upload_tugas(request):
    templates = 'grades/upload_tugas.html'
    if request.method == 'POST':
        form = TugasForm(request.POST, request.FILES)
        if form.is_valid():
            tugas = form.save(commit=False)
            tugas.mahasiswa = request.user
            # Ambil hash terakhir untuk previous_hash
            last_tugas = Tugas.objects.last()
            tugas.previous_hash = last_tugas.hash_tugas if last_tugas else '0' * 64
            tugas.save()
            return redirect('list_tugas')
    else:
        form = TugasForm()
    return render(request, templates, {'form': form})

@login_required
def input_nilai(request, tugas_id):
    templates = 'grades/input_nilai.html'
    tugas = Tugas.objects.get(id=tugas_id)
    if request.method == 'POST':
        form = NilaiForm(request.POST)
        if form.is_valid():
            nilai = form.save(commit=False)
            nilai.tugas = tugas

            # Enkripsi nilai
            rsa_private_key, _ = load_keys()
            nilai_asli = form.cleaned_data['nilai_asli']
            nilai.nilai_terenkripsi = encrypt_nilai(nilai_asli, rsa_private_key.public_key())

            nilai.save()
            return redirect('list_nilai')
    else:
        form = NilaiForm()
    return render(request, templates, {'form': form})

def verifikasi_nilai(request, nilai_id):
    templates = 'grades/verifikasi_nilai.html'
    nilai = Nilai.objects.get(id=nilai_id)
    _, ecdsa_public_key = load_keys()

    # Verifikasi tanda tangan
    is_valid = verify_signature(
        data=f"{nilai.tugas.hash_tugas}{nilai.nilai_terenkripsi}{nilai.timestamp}",
        signature=nilai.signature,
        public_key=ecdsa_public_key
    )

    return render(request, templates, {
        'nilai': nilai,
        'is_valid': is_valid
    })


def list_tugas(request):
    templates = 'grades/list_tugas.html'
    tugas_list = Tugas.objects.filter(mahasiswa=request.user)
    return render(request, templates, {'tugas_list': tugas_list})
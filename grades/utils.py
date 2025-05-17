from cryptography.hazmat.primitives import serialization
from django.conf import settings
import os

def load_keys():
    # Membaca kunci dari file
    with open(os.path.join(settings.BASE_DIR, 'keys/rsa_private.pem'), 'rb') as f:
        rsa_private_key = serialization.load_pem_private_key(f.read(), password=None)

    with open(os.path.join(settings.BASE_DIR, 'keys/ecdsa_public.pem'), 'rb') as f:
        ecdsa_public_key = serialization.load_pem_public_key(f.read())

    return rsa_private_key, ecdsa_public_key

def encrypt_nilai(nilai, public_key):
    # Implementasi enkripsi nilai
    pass

def verify_signature(data, signature, public_key):
    # Implementasi verifikasi tanda tangan
    pass
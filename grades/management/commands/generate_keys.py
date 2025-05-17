# grades/management/commands/generate_keys.py
from django.core.management.base import BaseCommand
from cryptography.hazmat.primitives.asymmetric import rsa, ec
import os

class Command(BaseCommand):
    help = 'Generate RSA and ECDSA key pairs'

    def handle(self, *args, **options):
        # Generate keys
        rsa_private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        ecdsa_private_key = ec.generate_private_key(ec.SECP256R1())

        # Simpan kunci ke file
        # ... implementasi penyimpanan kunci ...

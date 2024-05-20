from django.core import signing
from django.core.exceptions import PermissionDenied


def sign(salt, data):
    return signing.Signer(salt=salt).sign(data)


def unsign(salt, data):
    try:
        return signing.Signer(salt=salt).unsign(data)
    except signing.BadSignature:
        raise PermissionDenied()

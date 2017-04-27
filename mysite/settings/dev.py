from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-!#fntz2t96s8jt!hal)$3m#*i4@_et2^rrq3sl%rk64jb39(r'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# Maildump configuration
EMAIL_HOST = '127.0.0.1'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 1025
EMAIL_USE_TLS = False


try:
    from .local import *
except ImportError:
    pass

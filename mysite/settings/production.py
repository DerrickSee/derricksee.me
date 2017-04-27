from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False



# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

SECRET_KEY = os.environ.get('SECRET_KEY')

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
COMPRESS_CSS_HASHING_METHOD = 'content'

AWS_STORAGE_BUCKET_NAME = 'derricksee-media'
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

WAGTAILFRONTENDCACHE = {
    'cloudfront': {
        'BACKEND': 'wagtail.contrib.wagtailfrontendcache.backends.CloudfrontBackend',
        'DISTRIBUTION_ID': os.environ.get('CLOUDFRONT_DISTRIBUTION_ID'),
    },
}

SPARKPOST_API_KEY = os.environ.get('SPARKPOST_API_KEY')
EMAIL_BACKEND = 'sparkpost.django.email_backend.SparkPostEmailBackend'


try:
    from .local import *
except ImportError:
    pass

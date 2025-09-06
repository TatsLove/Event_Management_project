import os
import dj_database_url

DEBUG = os.getenv('DEBUG', 'True') == 'True'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(' ') if not DEBUG else []

DATABASES = {
  'default': dj_database_url.parse(os.getenv('DATABASE_URL'))
}

STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'
MIDDLEWARE = ['whitenoise.middleware.WhiteNoiseMiddleware'] + MIDDLEWARE

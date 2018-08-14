"""
Django settings for dining project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from dining.settings.components import BASE_DIR

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
with open(os.path.join(BASE_DIR, 'secret_key.txt')) as f:
    SECRET_KEY = f.read().strip()

with open(os.path.join(BASE_DIR, 'db.txt')) as f:
    db_pass = f.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['dt.anmolw.com']

# HTTPS

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dining',
        'USER': 'dining',
        'PASSWORD': db_pass,
        'HOST': 'localhost',
        'PORT': '',
    }
}

from mysite.settings import *
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^4t8qu@p2s^nzf2+7_-$$&vzncz14f$y65@#&&w9hdhkrom)if'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


#INSTALLED_APPS=[]

# sites framework
SITE_ID = 2


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



STATIC_ROOT = BASE_DIR/'static/'
MEDIA_ROOT = BASE_DIR/'media/'

STATICFILES_DIRS=[
    BASE_DIR/"statics",
    
]


#CSRF_COOKIE_SECURE = True
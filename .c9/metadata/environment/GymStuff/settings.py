{"filter":false,"title":"settings.py","tooltip":"/GymStuff/settings.py","undoManager":{"mark":81,"position":81,"stack":[[{"start":{"row":22,"column":14},"end":{"row":22,"column":18},"action":"remove","lines":["si1q"],"id":2},{"start":{"row":22,"column":14},"end":{"row":22,"column":31},"action":"insert","lines":["-l2(2xllph(=tjp#t"]},{"start":{"row":22,"column":32},"end":{"row":22,"column":37},"action":"remove","lines":["o&e*_"]},{"start":{"row":22,"column":32},"end":{"row":22,"column":37},"action":"insert","lines":["5+p2t"]},{"start":{"row":22,"column":38},"end":{"row":22,"column":39},"action":"remove","lines":["m"]},{"start":{"row":22,"column":38},"end":{"row":22,"column":39},"action":"insert","lines":["n"]},{"start":{"row":22,"column":40},"end":{"row":22,"column":57},"action":"remove","lines":["w_k5yg6_0sr6v1d0l"]},{"start":{"row":22,"column":41},"end":{"row":22,"column":44},"action":"remove","lines":["$o*"]},{"start":{"row":22,"column":41},"end":{"row":22,"column":44},"action":"insert","lines":["u^("]},{"start":{"row":22,"column":45},"end":{"row":22,"column":52},"action":"remove","lines":["6&f$(73"]},{"start":{"row":22,"column":45},"end":{"row":22,"column":47},"action":"insert","lines":["8_"]},{"start":{"row":22,"column":48},"end":{"row":22,"column":49},"action":"remove","lines":["f"]},{"start":{"row":22,"column":48},"end":{"row":22,"column":50},"action":"insert","lines":["#t"]},{"start":{"row":22,"column":51},"end":{"row":22,"column":54},"action":"remove","lines":["=u="]},{"start":{"row":22,"column":51},"end":{"row":22,"column":52},"action":"insert","lines":["5"]},{"start":{"row":22,"column":53},"end":{"row":22,"column":54},"action":"remove","lines":["y"]},{"start":{"row":22,"column":53},"end":{"row":22,"column":64},"action":"insert","lines":["j03)qviaog+"]}],[{"start":{"row":27,"column":17},"end":{"row":27,"column":84},"action":"insert","lines":["cc733d2ddeac4332a558149b1b1033a4.vfs.cloud9.eu-west-1.amazonaws.com"],"id":3}],[{"start":{"row":27,"column":84},"end":{"row":27,"column":85},"action":"insert","lines":["'"],"id":4}],[{"start":{"row":27,"column":17},"end":{"row":27,"column":18},"action":"insert","lines":["'"],"id":5}],[{"start":{"row":22,"column":13},"end":{"row":22,"column":43},"action":"insert","lines":["= os.environ.get('SECRET_KEY')"],"id":6}],[{"start":{"row":22,"column":43},"end":{"row":22,"column":95},"action":"remove","lines":["'-l2(2xllph(=tjp#ta5+p2tmnz2u^(l8_$#t%5dj03)qviaog+'"],"id":7}],[{"start":{"row":22,"column":13},"end":{"row":22,"column":14},"action":"remove","lines":["="],"id":8},{"start":{"row":22,"column":12},"end":{"row":22,"column":13},"action":"remove","lines":[" "]}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"insert","lines":["i"],"id":9},{"start":{"row":13,"column":1},"end":{"row":13,"column":2},"action":"insert","lines":["m"]},{"start":{"row":13,"column":2},"end":{"row":13,"column":3},"action":"insert","lines":["p"]},{"start":{"row":13,"column":3},"end":{"row":13,"column":4},"action":"insert","lines":["o"]},{"start":{"row":13,"column":4},"end":{"row":13,"column":5},"action":"insert","lines":["r"]},{"start":{"row":13,"column":5},"end":{"row":13,"column":6},"action":"insert","lines":["t"]}],[{"start":{"row":13,"column":6},"end":{"row":13,"column":7},"action":"insert","lines":[" "],"id":10},{"start":{"row":13,"column":7},"end":{"row":13,"column":8},"action":"insert","lines":["e"]},{"start":{"row":13,"column":8},"end":{"row":13,"column":9},"action":"insert","lines":["n"]},{"start":{"row":13,"column":9},"end":{"row":13,"column":10},"action":"insert","lines":["v"]}],[{"start":{"row":13,"column":10},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":11}],[{"start":{"row":0,"column":0},"end":{"row":121,"column":0},"action":"remove","lines":["\"\"\"","Django settings for GymStuff project.","","Generated by 'django-admin startproject' using Django 1.11.29.","","For more information on this file, see","https://docs.djangoproject.com/en/1.11/topics/settings/","","For the full list of settings and their values, see","https://docs.djangoproject.com/en/1.11/ref/settings/","\"\"\"","","import os","import env","","# Build paths inside the project like this: os.path.join(BASE_DIR, ...)","BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))","","","# Quick-start development settings - unsuitable for production","# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/","","# SECURITY WARNING: keep the secret key used in production secret!","SECRET_KEY = os.environ.get('SECRET_KEY')","","# SECURITY WARNING: don't run with debug turned on in production!","DEBUG = True","","ALLOWED_HOSTS = ['cc733d2ddeac4332a558149b1b1033a4.vfs.cloud9.eu-west-1.amazonaws.com']","","","# Application definition","","INSTALLED_APPS = [","    'django.contrib.admin',","    'django.contrib.auth',","    'django.contrib.contenttypes',","    'django.contrib.sessions',","    'django.contrib.messages',","    'django.contrib.staticfiles',","]","","MIDDLEWARE = [","    'django.middleware.security.SecurityMiddleware',","    'django.contrib.sessions.middleware.SessionMiddleware',","    'django.middleware.common.CommonMiddleware',","    'django.middleware.csrf.CsrfViewMiddleware',","    'django.contrib.auth.middleware.AuthenticationMiddleware',","    'django.contrib.messages.middleware.MessageMiddleware',","    'django.middleware.clickjacking.XFrameOptionsMiddleware',","]","","ROOT_URLCONF = 'GymStuff.urls'","","TEMPLATES = [","    {","        'BACKEND': 'django.template.backends.django.DjangoTemplates',","        'DIRS': [],","        'APP_DIRS': True,","        'OPTIONS': {","            'context_processors': [","                'django.template.context_processors.debug',","                'django.template.context_processors.request',","                'django.contrib.auth.context_processors.auth',","                'django.contrib.messages.context_processors.messages',","            ],","        },","    },","]","","WSGI_APPLICATION = 'GymStuff.wsgi.application'","","","# Database","# https://docs.djangoproject.com/en/1.11/ref/settings/#databases","","DATABASES = {","    'default': {","        'ENGINE': 'django.db.backends.sqlite3',","        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","    }","}","","","# Password validation","# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators","","AUTH_PASSWORD_VALIDATORS = [","    {","        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',","    },","    {","        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',","    },","    {","        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',","    },","    {","        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',","    },","]","","","# Internationalization","# https://docs.djangoproject.com/en/1.11/topics/i18n/","","LANGUAGE_CODE = 'en-us'","","TIME_ZONE = 'UTC'","","USE_I18N = True","","USE_L10N = True","","USE_TZ = True","","","# Static files (CSS, JavaScript, Images)","# https://docs.djangoproject.com/en/1.11/howto/static-files/","","STATIC_URL = '/static/'",""],"id":12},{"start":{"row":0,"column":0},"end":{"row":165,"column":0},"action":"insert","lines":["","\"\"\"","Django settings for ecommerce project.","Generated by 'django-admin startproject' using Django 1.11.15.","For more information on this file, see","https://docs.djangoproject.com/en/1.11/topics/settings/","For the full list of settings and their values, see","https://docs.djangoproject.com/en/1.11/ref/settings/","\"\"\"","","import os","import env","import dj_database_url","","# Build paths inside the project like this: os.path.join(BASE_DIR, ...)","BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))","","","# Quick-start development settings - unsuitable for production","# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/","","# SECURITY WARNING: keep the secret key used in production secret!","SECRET_KEY = os.environ.get('SECRET_KEY')","","# SECURITY WARNING: don't run with debug turned on in production!","DEBUG = True","","ALLOWED_HOSTS = [os.environ.get('HOSTNAME'), 'milestone-project5-gymcommerce.herokuapp.com']","","# Application definition","","INSTALLED_APPS = [","    'django.contrib.admin',","    'django.contrib.auth',","    'django.contrib.contenttypes',","    'django.contrib.sessions',","    'django.contrib.messages',","    'django.contrib.staticfiles',","    'django_forms_bootstrap',","    'accounts',","    'products',","    'cart',","    'checkout',","    'storages',","]","","MIDDLEWARE = [","    'django.middleware.security.SecurityMiddleware',","    'django.contrib.sessions.middleware.SessionMiddleware',","    'django.middleware.common.CommonMiddleware',","    'django.middleware.csrf.CsrfViewMiddleware',","    'django.contrib.auth.middleware.AuthenticationMiddleware',","    'django.contrib.messages.middleware.MessageMiddleware',","    'django.middleware.clickjacking.XFrameOptionsMiddleware',","]","","ROOT_URLCONF = 'ecommerce.urls'","","TEMPLATES = [","    {","        'BACKEND': 'django.template.backends.django.DjangoTemplates',","        'DIRS': [os.path.join(BASE_DIR, 'templates')],","        'APP_DIRS': True,","        'OPTIONS': {","            'context_processors': [","                'django.template.context_processors.debug',","                'django.template.context_processors.request',","                'django.contrib.auth.context_processors.auth',","                'django.contrib.messages.context_processors.messages',","                'django.template.context_processors.media',","                'cart.contexts.cart_contents'","            ],","        },","    },","]","","WSGI_APPLICATION = 'ecommerce.wsgi.application'","","","# Database","# https://docs.djangoproject.com/en/1.11/ref/settings/#databases","","if \"DATABASE_URL\" in os.environ:","    DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL')) }","else:","    print(\"Database URL not found. Using SQLite instead\")","    DATABASES = {","        'default': {","            'ENGINE': 'django.db.backends.sqlite3',","            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","        }","    }  ","","# Password validation","# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators","","AUTH_PASSWORD_VALIDATORS = [","    {","        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',","    },","    {","        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',","    },","    {","        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',","    },","    {","        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',","    },","]","","AUTHENTICATION_BACKENDS = [","    'django.contrib.auth.backends.ModelBackend',","    'accounts.backends.CaseInsensitiveAuth'","]","","# Internationalization","# https://docs.djangoproject.com/en/1.11/topics/i18n/","","LANGUAGE_CODE = 'en-us'","","TIME_ZONE = 'UTC'","","USE_I18N = True","","USE_L10N = True","","USE_TZ = True","","","# Static files (CSS, JavaScript, Images)","# https://docs.djangoproject.com/en/1.11/howto/static-files/","","AWS_S3_OBJECT_PARAMETERS = {","    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',","    'CacheControl': 'max-age=94608000'","}","","AWS_STORAGE_BUCKET_NAME = 'chris-m-ecommerce'","AWS_S3_REGION_NAME = 'eu-west-1'","AWS_ACCESS_KEY_ID = os.environ.get(\"AWS_ACCESS_KEY_ID\")","AWS_SECRET_ACCESS_KEY = os.environ.get(\"AWS_SECRET_ACCESS_KEY\")","","AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME","","STATICFILES_LOCATION = 'static'","STATICFILES_STORAGE = 'custom_storages.StaticStorage'","#'storages.backends.s3boto3.S3Boto3Storage'","#'custom_storages.StaticStorage'","","STATIC_URL = '/static/'","STATICFILES_DIRS = (","    os.path.join(BASE_DIR, \"static\"),",")","","MEDIAFILES_LOCATION = 'media'","DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'","","MEDIA_ROOT = os.path.join(BASE_DIR, 'media')","MEDIA_URL = \"https://%s/%s/\" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)","","STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE')","STRIPE_SECRET = os.getenv('STRIPE_SECRET')","","MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'",""]}],[{"start":{"row":2,"column":20},"end":{"row":2,"column":29},"action":"remove","lines":["ecommerce"],"id":13},{"start":{"row":2,"column":20},"end":{"row":2,"column":28},"action":"insert","lines":["GymStuff"]}],[{"start":{"row":56,"column":16},"end":{"row":56,"column":25},"action":"remove","lines":["ecommerce"],"id":14},{"start":{"row":56,"column":16},"end":{"row":56,"column":24},"action":"insert","lines":["GymStuff"]}],[{"start":{"row":76,"column":20},"end":{"row":76,"column":29},"action":"remove","lines":["ecommerce"],"id":15},{"start":{"row":76,"column":20},"end":{"row":76,"column":28},"action":"insert","lines":["GymStuff"]}],[{"start":{"row":138,"column":26},"end":{"row":138,"column":41},"action":"insert","lines":["os.environ.get("],"id":16}],[{"start":{"row":139,"column":21},"end":{"row":139,"column":36},"action":"insert","lines":["os.environ.get("],"id":17}],[{"start":{"row":138,"column":41},"end":{"row":138,"column":42},"action":"insert","lines":["\""],"id":18},{"start":{"row":138,"column":42},"end":{"row":138,"column":43},"action":"insert","lines":["\""]}],[{"start":{"row":138,"column":42},"end":{"row":138,"column":66},"action":"insert","lines":["AWS_STORAGE_BUCKET_NAME "],"id":19}],[{"start":{"row":138,"column":67},"end":{"row":138,"column":68},"action":"insert","lines":[")"],"id":20}],[{"start":{"row":138,"column":65},"end":{"row":138,"column":66},"action":"remove","lines":[" "],"id":21}],[{"start":{"row":139,"column":36},"end":{"row":139,"column":37},"action":"insert","lines":["\""],"id":22}],[{"start":{"row":139,"column":37},"end":{"row":139,"column":55},"action":"insert","lines":["AWS_S3_REGION_NAME"],"id":23}],[{"start":{"row":139,"column":55},"end":{"row":139,"column":56},"action":"insert","lines":["\""],"id":24},{"start":{"row":139,"column":56},"end":{"row":139,"column":57},"action":"insert","lines":[")"]}],[{"start":{"row":139,"column":57},"end":{"row":139,"column":68},"action":"remove","lines":["'eu-west-1'"],"id":25}],[{"start":{"row":138,"column":67},"end":{"row":138,"column":86},"action":"remove","lines":["'chris-m-ecommerce'"],"id":26}],[{"start":{"row":11,"column":0},"end":{"row":11,"column":1},"action":"insert","lines":["#"],"id":27}],[{"start":{"row":11,"column":0},"end":{"row":11,"column":1},"action":"remove","lines":["#"],"id":28}],[{"start":{"row":147,"column":0},"end":{"row":148,"column":32},"action":"remove","lines":["#'storages.backends.s3boto3.S3Boto3Storage'","#'custom_storages.StaticStorage'"],"id":29},{"start":{"row":146,"column":53},"end":{"row":147,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":145,"column":0},"end":{"row":145,"column":1},"action":"insert","lines":["#"],"id":30}],[{"start":{"row":146,"column":0},"end":{"row":146,"column":1},"action":"insert","lines":["#"],"id":31}],[{"start":{"row":145,"column":0},"end":{"row":145,"column":1},"action":"remove","lines":["#"],"id":32}],[{"start":{"row":146,"column":0},"end":{"row":146,"column":1},"action":"remove","lines":["#"],"id":33}],[{"start":{"row":37,"column":33},"end":{"row":38,"column":0},"action":"insert","lines":["",""],"id":34},{"start":{"row":38,"column":0},"end":{"row":38,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":38,"column":4},"end":{"row":38,"column":6},"action":"insert","lines":["''"],"id":35}],[{"start":{"row":38,"column":6},"end":{"row":38,"column":7},"action":"insert","lines":[","],"id":36}],[{"start":{"row":38,"column":5},"end":{"row":38,"column":25},"action":"insert","lines":["django.contrib.sites"],"id":37}],[{"start":{"row":44,"column":15},"end":{"row":45,"column":0},"action":"insert","lines":["",""],"id":38},{"start":{"row":45,"column":0},"end":{"row":45,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":45,"column":4},"end":{"row":45,"column":6},"action":"insert","lines":["''"],"id":39}],[{"start":{"row":45,"column":6},"end":{"row":45,"column":7},"action":"insert","lines":[","],"id":40}],[{"start":{"row":45,"column":5},"end":{"row":45,"column":14},"action":"insert","lines":["'reviews'"],"id":41}],[{"start":{"row":45,"column":13},"end":{"row":45,"column":15},"action":"remove","lines":["''"],"id":42}],[{"start":{"row":45,"column":13},"end":{"row":45,"column":14},"action":"insert","lines":["'"],"id":43}],[{"start":{"row":45,"column":4},"end":{"row":45,"column":6},"action":"remove","lines":["''"],"id":44}],[{"start":{"row":45,"column":4},"end":{"row":45,"column":5},"action":"insert","lines":["'"],"id":45}],[{"start":{"row":37,"column":33},"end":{"row":38,"column":27},"action":"remove","lines":["","    'django.contrib.sites',"],"id":46}],[{"start":{"row":43,"column":15},"end":{"row":44,"column":14},"action":"remove","lines":["","    'reviews',"],"id":47}],[{"start":{"row":43,"column":15},"end":{"row":44,"column":0},"action":"insert","lines":["",""],"id":48},{"start":{"row":44,"column":0},"end":{"row":44,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":44,"column":4},"end":{"row":44,"column":6},"action":"insert","lines":["''"],"id":49}],[{"start":{"row":44,"column":5},"end":{"row":44,"column":6},"action":"insert","lines":["c"],"id":50},{"start":{"row":44,"column":6},"end":{"row":44,"column":7},"action":"insert","lines":["u"]}],[{"start":{"row":44,"column":7},"end":{"row":44,"column":8},"action":"insert","lines":["s"],"id":51},{"start":{"row":44,"column":8},"end":{"row":44,"column":9},"action":"insert","lines":["t"]},{"start":{"row":44,"column":9},"end":{"row":44,"column":10},"action":"insert","lines":["o"]},{"start":{"row":44,"column":10},"end":{"row":44,"column":11},"action":"insert","lines":["m"]},{"start":{"row":44,"column":11},"end":{"row":44,"column":12},"action":"insert","lines":["e"]},{"start":{"row":44,"column":12},"end":{"row":44,"column":13},"action":"insert","lines":["r"]},{"start":{"row":44,"column":13},"end":{"row":44,"column":14},"action":"insert","lines":["_"]}],[{"start":{"row":44,"column":14},"end":{"row":44,"column":15},"action":"insert","lines":["r"],"id":52},{"start":{"row":44,"column":15},"end":{"row":44,"column":16},"action":"insert","lines":["e"]},{"start":{"row":44,"column":16},"end":{"row":44,"column":17},"action":"insert","lines":["v"]},{"start":{"row":44,"column":17},"end":{"row":44,"column":18},"action":"insert","lines":["i"]},{"start":{"row":44,"column":18},"end":{"row":44,"column":19},"action":"insert","lines":["e"]},{"start":{"row":44,"column":19},"end":{"row":44,"column":20},"action":"insert","lines":["w"]},{"start":{"row":44,"column":20},"end":{"row":44,"column":21},"action":"insert","lines":["s"]}],[{"start":{"row":44,"column":22},"end":{"row":44,"column":23},"action":"insert","lines":[","],"id":53}],[{"start":{"row":164,"column":0},"end":{"row":165,"column":0},"action":"insert","lines":["",""],"id":54}],[{"start":{"row":165,"column":0},"end":{"row":169,"column":54},"action":"insert","lines":["EMAIL_USE_TLS = True","EMAIL_HOST = 'smtp.gmail.com'","EMAIL_PORT = 587","EMAIL_HOST_USER = os.environ.get(\"EMAIL_ADDRESS\")","EMAIL_HOST_PASSWORD = os.environ.get(\"EMAIL_PASSWORD\")"],"id":55}],[{"start":{"row":164,"column":0},"end":{"row":165,"column":45},"action":"insert","lines":["EMAIL_BACKEND =","‘django.core.mail.backends.smtp.EmailBackend’"],"id":56}],[{"start":{"row":164,"column":15},"end":{"row":165,"column":0},"action":"remove","lines":["",""],"id":57}],[{"start":{"row":164,"column":15},"end":{"row":164,"column":16},"action":"remove","lines":["‘"],"id":58}],[{"start":{"row":164,"column":15},"end":{"row":164,"column":16},"action":"insert","lines":["'"],"id":59}],[{"start":{"row":164,"column":59},"end":{"row":164,"column":60},"action":"remove","lines":["’"],"id":60}],[{"start":{"row":164,"column":59},"end":{"row":164,"column":60},"action":"insert","lines":["'"],"id":61}],[{"start":{"row":163,"column":74},"end":{"row":164,"column":0},"action":"insert","lines":["",""],"id":62}],[{"start":{"row":165,"column":0},"end":{"row":165,"column":1},"action":"insert","lines":["#"],"id":63}],[{"start":{"row":170,"column":54},"end":{"row":171,"column":0},"action":"insert","lines":["",""],"id":64},{"start":{"row":171,"column":0},"end":{"row":172,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":172,"column":0},"end":{"row":175,"column":1},"action":"insert","lines":["AUTHENTICATION_BACKENDS = [","    'django.contrib.auth.backends.ModelBackend',","    'accounts.backends.EmailAuth'","]"],"id":65}],[{"start":{"row":175,"column":1},"end":{"row":176,"column":0},"action":"insert","lines":["",""],"id":66}],[{"start":{"row":165,"column":0},"end":{"row":176,"column":0},"action":"remove","lines":["#EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'","EMAIL_USE_TLS = True","EMAIL_HOST = 'smtp.gmail.com'","EMAIL_PORT = 587","EMAIL_HOST_USER = os.environ.get(\"EMAIL_ADDRESS\")","EMAIL_HOST_PASSWORD = os.environ.get(\"EMAIL_PASSWORD\")","","AUTHENTICATION_BACKENDS = [","    'django.contrib.auth.backends.ModelBackend',","    'accounts.backends.EmailAuth'","]",""],"id":67},{"start":{"row":165,"column":0},"end":{"row":177,"column":1},"action":"insert","lines":["","","EMAIL_USE_TLS = True","EMAIL_HOST = 'smtp.gmail.com'","EMAIL_PORT = 587","EMAIL_HOST_USER = os.environ.get(\"EMAIL_ADDRESS\")","EMAIL_HOST_PASSWORD = os.environ.get(\"EMAIL_PASSWORD\")","","","AUTHENTICATION_BACKENDS = [","    'django.contrib.auth.backends.ModelBackend',","    'accounts.backends.EmailAuth'","]"]}],[{"start":{"row":177,"column":1},"end":{"row":178,"column":0},"action":"insert","lines":["",""],"id":68}],[{"start":{"row":165,"column":0},"end":{"row":166,"column":0},"action":"remove","lines":["",""],"id":69},{"start":{"row":164,"column":0},"end":{"row":165,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":164,"column":0},"end":{"row":165,"column":0},"action":"insert","lines":["",""],"id":70}],[{"start":{"row":165,"column":0},"end":{"row":170,"column":54},"action":"insert","lines":["EMAIL_USE_TLS = True","EMAIL_USE_SSL = False","EMAIL_HOST = 'smtp.gmail.com'","EMAIL_PORT = 587","EMAIL_HOST_USER = os.environ.get(\"EMAIL_ADDRESS\")","EMAIL_HOST_PASSWORD = os.environ.get(\"EMAIL_PASSWORD\")"],"id":71}],[{"start":{"row":171,"column":0},"end":{"row":175,"column":54},"action":"remove","lines":["EMAIL_USE_TLS = True","EMAIL_HOST = 'smtp.gmail.com'","EMAIL_PORT = 587","EMAIL_HOST_USER = os.environ.get(\"EMAIL_ADDRESS\")","EMAIL_HOST_PASSWORD = os.environ.get(\"EMAIL_PASSWORD\")"],"id":72}],[{"start":{"row":171,"column":0},"end":{"row":172,"column":0},"action":"remove","lines":["",""],"id":73}],[{"start":{"row":171,"column":0},"end":{"row":172,"column":0},"action":"remove","lines":["",""],"id":74}],[{"start":{"row":75,"column":1},"end":{"row":76,"column":0},"action":"insert","lines":["",""],"id":75}],[{"start":{"row":76,"column":0},"end":{"row":79,"column":70},"action":"insert","lines":["                'django.template.context_processors.debug',","                'django.template.context_processors.request',","                'django.contrib.auth.context_processors.auth',","                'django.contrib.messages.context_processors.messages',"],"id":76}],[{"start":{"row":76,"column":0},"end":{"row":79,"column":70},"action":"remove","lines":["                'django.template.context_processors.debug',","                'django.template.context_processors.request',","                'django.contrib.auth.context_processors.auth',","                'django.contrib.messages.context_processors.messages',"],"id":77},{"start":{"row":75,"column":1},"end":{"row":76,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":171,"column":0},"end":{"row":171,"column":2},"action":"insert","lines":["\"\""],"id":78}],[{"start":{"row":171,"column":2},"end":{"row":171,"column":3},"action":"insert","lines":["\""],"id":79}],[{"start":{"row":175,"column":1},"end":{"row":176,"column":0},"action":"insert","lines":["",""],"id":80}],[{"start":{"row":176,"column":0},"end":{"row":176,"column":2},"action":"insert","lines":["\"\""],"id":81}],[{"start":{"row":176,"column":2},"end":{"row":176,"column":3},"action":"insert","lines":["\""],"id":82}],[{"start":{"row":171,"column":0},"end":{"row":176,"column":3},"action":"remove","lines":["\"\"\"","AUTHENTICATION_BACKENDS = [","    'django.contrib.auth.backends.ModelBackend',","    'accounts.backends.EmailAuth'","]","\"\"\""],"id":83}]]},"ace":{"folds":[],"scrolltop":2115,"scrollleft":0,"selection":{"start":{"row":171,"column":0},"end":{"row":171,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":150,"state":"start","mode":"ace/mode/python"}},"timestamp":1595872864855,"hash":"0318bc97c0e69482354ef5756bdd40ba98f42255"}
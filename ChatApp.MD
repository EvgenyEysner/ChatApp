1. pip install django
2. django-admin startproject core .
3. python manage.py startapp chat
4. change settings in settings.py
   example https://github.com/Monk3y1980/DjangoChat/blob/master/core/settings.py
5. add chat to core/ settings > INSTALLED_APPS
6. add .gitignore > git init
7. git add . (add all files except .gitignore)
8. pip install Pillow 
9. python manage.py startapp accounts
10. Create Models CustomUser
11. Create Models Message, Room
12. add accounts to core/ settings > INSTALLED_APPS
13. Create Models CustomUser -> python manage.py makemigrations -> python manage.py migrate
14. Create Superuser python manage.py createsuperuser
15. pip install drf-yasg
16. pip install djangorestframework
17. pip install channels
18. pip install django-cors-headers
19. add 'rest_framework', 'channels', 'drf_yasg', 'corsheaders', 'django.contrib.staticfiles', # required for serving swagger ui's css/js files 
to core/ settings > INSTALLED_APPS
20. 
``` 
   MIDDLEWARE = [
    ...,
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    ...,
]
```
21. 
```
   CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "https://sub.example.com",
    "http://localhost:8000",
    "http://127.0.0.1:3000",
]
```
23. 
```
   REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
```
24. python3 -m pip install channels_redis
```
# Channels
ASGI_APPLICATION = 'core.asgi.application'

# для Redis
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}

```

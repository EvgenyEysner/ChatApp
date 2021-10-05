from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .yasg import urlpatterns as doc_urls

urlpatterns = [
    #    path('', include(router.urls)),
#     path('', include('frontend.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='api')),
    # path('api/v1/', include('chat.urls')),
    # path('api/v1/', include('accounts.urls')),
]

urlpatterns += doc_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from root import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('shop/', include('app.urls')),
                  path('', include('users.urls')),
                  path('social-auth/',
                       include('social_django.urls', namespace='social')),
                  path('api-auth/', include('rest_framework.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

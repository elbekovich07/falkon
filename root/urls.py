from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from root import settings

import app

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('shop/', include('app.urls')),
                  path('users/', include('users.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

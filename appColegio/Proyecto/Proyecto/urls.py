from django.contrib import admin
from django.urls import path, include
from AppColegio import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app-colegio/', include('AppColegio.urls')),
    path('', views.index)
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path, include  # asegúrate de importar include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # panel de administración
    path('admin/', admin.site.urls),

    # vistas de login/logout/password reset que Django ofrece por defecto
    path('accounts/', include('django.contrib.auth.urls')),

    # todas las rutas de tu app "core"
    path('', include('core.urls')),
]

#Archivos estátios

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


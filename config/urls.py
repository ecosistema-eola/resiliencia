from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

def healthz(request):
    return HttpResponse("OK")

urlpatterns = [
    # healthcheck obligatorio para Railway
    path("healthz/", healthz, name="healthz"),

    # panel de administración
    path('admin/', admin.site.urls),

    # login/logout/password-reset
    path('accounts/', include('django.contrib.auth.urls')),

    # tu aplicación principal
    path('', include('core.urls')),
]

# servir media en desarrollo/production si lo necesitas
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

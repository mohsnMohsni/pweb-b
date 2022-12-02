# Core imports.
from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Local imports.
from extensions.yasg import urlpatterns as docs_urlpatterns


urlpatterns = [
    path('accounts/', include('apps.accounts.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += docs_urlpatterns

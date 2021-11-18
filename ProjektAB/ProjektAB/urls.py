from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from django.conf.urls.static import static
from ProjektAB import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('league/', include('league.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
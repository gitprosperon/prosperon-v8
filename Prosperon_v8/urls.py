from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'accounts/', include('Accounts.urls')),
    path(r'budget/', include('Budget.urls')),
    path(r'', include('MainWebsite.urls')),
    path(r'', include('Student.urls')),
    path(r'anytime-decision/', include('Student.anytime_decision_urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

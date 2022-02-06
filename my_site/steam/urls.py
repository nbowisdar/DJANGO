from django.urls import path
from steam.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('test/', funk),
    path('', pattern),
    path('test_temp', test_template)
]# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
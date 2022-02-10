from django.urls import path
from steam.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('test/', funk),
    path('login', pattern, name='login'),
    path('test_temp', test_template),
    path('test_form', test_form, name='test_form'),
    path('test_new_form', test_new_login)
]# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
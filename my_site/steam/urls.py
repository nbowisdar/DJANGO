from django.urls import path, include
from steam.views import *
import django.contrib.auth.urls

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('test', funk),
    path('login', My_login.as_view()),
    path('test_temp', test_template),
    path('test_form', test_form, name='test_form'),
    path('register', RegisterUser.as_view()),
    path('test1', Test_View.as_view()),
    #path('new_form_reg', new_reg)

]# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
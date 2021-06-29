from django.urls import path
from userlogin import views
from django.conf.urls.static import static
from django.conf import settings
app_name= 'userlogin'

urlpatterns = [
    path('register/',views.Register, name='Register'),
    path('login/',views.Login, name='login'),
    path('home/',views.Home, name='home'),
    path('base/',views.base, name='base'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
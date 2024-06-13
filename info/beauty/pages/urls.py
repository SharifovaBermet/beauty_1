
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *

    
urlpatterns = [
   path('', home_page, name='home'),
   path('pricing/',pricing,name='pricing'),
   path('about/',about,name='about'),
   path('contact/',contact,name='contact'),
   path('specialists/',specialist,name='specialists'),
   path('blog/',blog,name='blog'),
   path('auth/',login_info,name='auth'),
   path('registrations/',registrations,name='registrations'),
   path('logout/',logout_info,name='logout')
   
    
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


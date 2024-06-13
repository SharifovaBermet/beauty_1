
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
   path('', home_page, name='home'),
   path('pricing/',pricing,name='pricing'),
   path('about/',about,name='about'),
   path('contact/',contact,name='contact'),
   path('specialists/',specialist,name='specialists'),
   path('blog/',blog,name='blog'),
   path('record/<int:id>/',record_info,name='record'),
   path('record/<int:id>/<int:pk>/',record_info_serivce,name='record'),
   path('auth/',login_info,name='auth'),
   path('registrations/',registrations,name='registrations'),
   path('logout/',logout_info,name='logout'),
   path('myaccount/',myaccount,name='myaccount'),
   path('myaccount_admin/',myaccount_admin,name='myaccount_admin'),
   path('myaccount_admin/<int:id>/',myaccount_admin_master,name='myaccount_admin'),
   path('pay_mbank/<int:id>/',pay_mbank,name='pay_mbank'),
   path('myaccount_dorector/',myaccount_dorector,name='myaccount_dorector'),
   
   path('master_graf/<int:id>',myaccount_admin_master_graf,name='master_graf'),
   path('master_graf/',myaccount_master_graf,name='master_graf'),
   path('myaccount_info/',myaccount_info,name='myaccount_info'),
   path('salons/',salons,name='salons'),
   path('salon/<int:id>/',salons_id,name='salons'),
   path('branchs/',branch,name='branch'),
   path('branch/<int:id>/',branch_id,name='branch'),
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


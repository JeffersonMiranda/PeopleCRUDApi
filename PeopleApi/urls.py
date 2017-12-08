"""
Definition of urls for PeopleApi.
"""

from datetime import datetime
from rest_framework.routers import DefaultRouter
from django.conf.urls import url
import django.contrib.auth.views
from app import views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

router = DefaultRouter()

router.register(r'persons',views.PersonView)
router.register(r'emails',views.EmailView)
router.register(r'addresses',views.AddressView)
router.register(r'phoneNumbers',views.PhoneNumberView)

urlpatterns = [    
    url(r'^', include(router.urls)),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]

from django.conf.urls import patterns, include, url
from lopa.signatures.views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', CreateSignature.as_view(), name='create'),
    url(r'^list$', IndexSignatures.as_view(), name='index'),
    url(r'^count$', 'lopa.signatures.views.count_signatures', name='count'),
    # url(r'^crum/', include('crum.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
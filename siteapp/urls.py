from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.conf import settings

urlpatterns = patterns(
    '',
    (r'^photoupload/$', 'webcam.views.upload_image'),
    (r'^photoupload/direct/$', 'webcam.views.make_direct'),

    (r'^$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            'path': 'index.html'
            }),

    (r'^(?P<path>(.*))$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT
            }),

    # Example:
    # (r'^siteappdjango/', include('siteappdjango.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)

# End

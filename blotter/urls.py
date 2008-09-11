from django.conf.urls.defaults import *
from crime_map.blotter.models import Crime

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.list_detail.object_list', dict(queryset=Crime.objects.all()), name="crime-list"),
    url(r'^type/$', 'django.views.generic.list_detail.object_list', dict(queryset=Crime.objects.all()), name="crime-list"),
    url(r'^type/(?P<crime_type>[-\w]+)/$', 'django.views.generic.list_detail.object_list', dict(queryset=Crime.objects.all()), name="crime-list"),
    url(r'^agency/$', 'django.views.generic.list_detail.object_list', dict(queryset=Crime.objects.all()), name="crime-list"),
    url(r'^agency/(?P<agency>[-\w]+)/$', 'django.views.generic.list_detail.object_list', dict(queryset=Crime.objects.all()), name="crime-list"),
)

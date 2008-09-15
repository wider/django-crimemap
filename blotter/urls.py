from django.conf.urls.defaults import *
from crime_map.blotter.models import Crime
from crime_map.blotter.views import by_type, by_agency

urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.list_detail.object_list', dict(queryset=Crime.objects.all()), name="crime-list"),

    # Crimes by Date
    url(r'^(?P<year>\d{4})/$', 'django.views.generic.date_based.archive_year', dict({'queryset':Crime.objects.all(), 'date_field':'date', 'make_object_list':True}), name="crime-list-by-year"),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$', 'django.views.generic.date_based.archive_month', dict({'queryset':Crime.objects.all(), 'date_field':'date'}), name="crime-list-by-month"),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{1,2})/$', 'django.views.generic.date_based.archive_day', dict({'queryset':Crime.objects.all(), 'date_field':'date'}), name="crime-list-by-day"),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{1,2})/(?P<object_id>\d+)/$', 'django.views.generic.date_based.object_detail', dict({'queryset':Crime.objects.all(), 'date_field':'date'}), name="crime-instance"),

    # Crimes by Type
    url(r'^type/$', 'django.views.generic.list_detail.object_list', dict(queryset=Crime.objects.all()), name="crime-type-list"),
    url(r'^type/(?P<crime_type>[-\w]+)/$', by_type, name="crime-type-filter"),

    # Crimes by Agency
    url(r'^agency/$', 'django.views.generic.list_detail.object_list', dict(queryset=Crime.objects.all()), name="crime-agency-list"),
    url(r'^agency/(?P<agency>[-\w]+)/$', 'django.views.generic.list_detail.object_list', dict(queryset=Crime.objects.all()), name="crime-agency-filter"),
)

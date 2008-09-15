from django.views.generic.list_detail import object_list
from crime_map.blotter.models import Crime


def by_type(request, crime_type):
    #import ipdb; ipdb.set_trace()
    print repr(crime_type)
    crimes = Crime.objects.filter(crime_type__slug=crime_type)
    return object_list(request, queryset=crimes)

def by_agency():
    pass

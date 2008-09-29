from django.views.generic.list_detail import object_list
from crime_map.blotter.models import Crime


def by_type(request, crime_type):
    crimes = Crime.objects.filter(crime_type__slug=crime_type)
    return object_list(request, queryset=crimes)

def by_agency(request, agency):
    crimes = Crime.objects.filter(agency__slug=agency)
    return object_list(request, queryset=crimes)

def in_date_range(request, start_date, end_date):
    crimes = Crime.objects.filter(date__range=(start_date, end_date)
    return object_list(request, queryset=crimes)

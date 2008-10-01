from django.views.generic.list_detail import object_list
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from crime_map.blotter.models import Crime
from crime_map.blotter.forms import DateRangeForm


def by_type(request, crime_type):
    crimes = Crime.objects.filter(crime_type__slug=crime_type)
    return object_list(request, queryset=crimes)

def by_agency(request, agency):
    crimes = Crime.objects.filter(agency__slug=agency)
    return object_list(request, queryset=crimes)

def in_date_range(request, start_date, end_date):
    crimes = Crime.objects.filter(date__range=(start_date, end_date))
    return object_list(request, queryset=crimes)

def filter_by_date(request):
    if request.method == "POST":
        f = DateRangeForm(request.POST)
        if f.is_valid():
            crimes = Crime.objects.filter(date__range=(f.cleaned_data['start_date'], f.cleaned_data['end_date']))
            return object_list(request, queryset=crimes)
        else:
            return HttpResponseRedirect(reverse('crime-list'))
    else:
        return HttpResponseRedirect(reverse('crime-list'))

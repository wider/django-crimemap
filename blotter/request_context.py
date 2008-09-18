from crime_map.blotter.models import CrimeType, Agency

def crime_types(request):
    return {'crimetypes':CrimeType.objects.all()}

def agencies(request):
    return {'agencies':Agency.objects.all()}

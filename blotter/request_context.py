from crime_map.blotter.models import CrimeType, Agency
from django.conf import settings

def crime_types(request):
    return {'crimetypes':CrimeType.objects.all()}

def agencies(request):
    return {'agencies':Agency.objects.all()}

def google_api_key(request):
    return {'GOOGLE_API_KEY':settings.GOOGLE_API_KEY}

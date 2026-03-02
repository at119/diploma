from django.conf import settings


def mapbox(request):
    return {"MAPBOX_ACCESS_TOKEN": getattr(settings, "MAPBOX_ACCESS_TOKEN", "")}

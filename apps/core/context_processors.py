import settings


def media_url(request):
    return {'media_url': settings.MEDIA_URL}
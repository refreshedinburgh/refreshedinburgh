from django.views.generic.date_based import archive_year

from apps.events.models import Location, Event


def event_archive(request):
    pass


def event_year_archive(request, year):
    return archive_year(request, year=year, queryset=Event.objects.all(),
        date_field='date', template_name='events/event_year_archive.html',
        allow_empty=False)


def event_detail(request, year, slug):
    pass

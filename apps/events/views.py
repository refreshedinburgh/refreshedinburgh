import datetime

from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.generic.date_based import archive_index, archive_year

from apps.events.models import Location, Event


def event_archive(request):
    upcoming_events = Event.objects.filter(date__gte=datetime.date.today())
    past_events = Event.objects.filter(date__lt=datetime.date.today())
    context = {
        'upcoming_events': upcoming_events,
        'past_events': past_events,
    }
    return render_to_response('events/event_archive.html',
        RequestContext(request, context))


def event_year_archive(request, year):
    return archive_year(request, year=year,
        queryset=Event.objects.all().select_related(), date_field='date',
        template_name='events/event_year_archive.html', allow_empty=False,
        make_object_list=True)


def event_detail(request, year, slug):
    event = get_object_or_404(Event.objects.all().select_related(),
        date__year=year, slug=slug)
    context = {
        'event': event,
    }
    return render_to_response('events/event_detail.html',
        RequestContext(request, context))

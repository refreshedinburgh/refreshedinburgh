import datetime

from django.contrib.syndication.feeds import Feed

from models import Event


class UpcomingEvents(Feed):
    title = "RefreshEdinburgh Events"
    link = "/events/"
    description = "Upcoming events organised by RefreshEdinburgh."

    def items(self):
        now = datetime.datetime.now()
        return Event.objects.filter(date__gte=now).order_by('date')[:5]

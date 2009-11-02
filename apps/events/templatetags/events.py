from django.template import Library, Node
from apps.events.models import Event


register = Library()


class LatestEventsNode(Node):
    def render(self, context):
        context['event_list'] = reversed(Event.objects.all().order_by('-date')[:3])
        return ''


@register.tag
def get_latest_events(parser, token):
    return LatestEventsNode()

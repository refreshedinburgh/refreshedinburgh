from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext


def home(request):
    return render_to_response('core/home.html', RequestContext(request))


def members(request):
    return render_to_response('core/members.html', RequestContext(request))


def jobs(request):
    return render_to_response('core/jobs.html', RequestContext(request))



from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader, RequestContext
from django.core.urlresolvers import reverse

from .forms import DocumentForm
from .models import Site, NetworkDevice, Interface, Credentials, CSVDownload

def index(request):
    sites = Site.objects.order_by('site_name')
    context = {'sites': sites}
    return render(request, 'send_command/index.html', context)

def detail(request, site_name):
    try:
        devices = NetworkDevice.objects.filter(site_id=site_name)
    except Site.DoesNotExist:
        raise Http404("%s does not exist" % site_name)
    return render(request, 'send_command/detail.html', {'devices': devices}) 


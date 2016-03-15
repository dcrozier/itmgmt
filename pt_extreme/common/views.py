from django.shortcuts import render
from django.template import loader

from send_command.models import Site, NetworkDevice, Interface, Credentials, CSVDownload

def index(request):
    return render(request, 'common/index.html')

def site_view(request):
    sites = Site.objects.order_by('site_name')
    context = {'sites': sites}
    return render(request, 'common/site_view.html', context)

def detail(request, site_name):
    try:
        devices = NetworkDevice.objects.filter(site_id=site_name)
    except Site.DoesNotExist:
        raise Http404("%s does not exist" % site_name)
    return render(request, 'common/site_detail.html', {'devices': devices})


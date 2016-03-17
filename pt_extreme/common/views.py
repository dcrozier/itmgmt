from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect

from common.models import RecentActions, Site, NetworkDevice, Credentials


def index(request):
    recent_actions = RecentActions.objects.order_by('id')
    context = {'recent_actions': recent_actions}
    return render(request, 'common/index.html', context)


def add_credentials(request):
    if request.method == 'POST':
        pass
    return render(request, 'common/add_credentials')


def site_view(request):
    sites = Site.objects.order_by('site_name')
    context = {'sites': sites}
    return render(request, 'common/site_view.html', context)


def create_site(request):
    if request.method == 'POST':
        site = Site.objects.get_or_create(
            site_name=request.POST.get('site_name'),
            site_group=request.POST.get('site_group'),
            site_template=request.FILES['site_template']
        )
        if not Credentials.DoesNotExist(request.POST.get('site_credentials')):
            site.site_credentials = Credentials.objects.get()
        RecentActions.objects.create(
            entry="Added Site %s to %s" % (request.POST.get('site_name'), request.POST.get('site_group'))
        )
        return HttpResponseRedirect('/')
    context = {'creds': Credentials.objects.all(), 'groups': [site for site in Site.objects.all()]}
    return render(request, 'common/create_site.html', context)


def detail(request, site_name):
    try:
        devices = NetworkDevice.objects.filter(site_id=site_name)
    except Site.DoesNotExist:
        raise Http404("%s does not exist" % site_name)
    return render(request, 'common/site_detail.html', {'devices': devices})

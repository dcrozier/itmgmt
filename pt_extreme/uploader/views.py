from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

import os
import csv

from models import Document
from send_command.models import NetworkDevice, Site, Credentials
from forms import DocumentForm

def upload(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()
            reader = csv.DictReader(request.FILES['docfile'])
            device={}
            for row in reader:
                device[request.POST.get('site_name')] = NetworkDevice.objects.get_or_create(
                        device_name     = row['device_name'],
                        device_type     = row['device_type'],
                        ip_address      = row['ip_address'],
                        port            = row['port'],
                        data_vlan       = row['data_vlan'],
                        voice_vlan      = row['voice_vlan'],
                        management_vlan = row['management_vlan'],
                        vendor          = row['vendor'],
                        model           = row['model'],
                        os_version      = row['os_version'],
                        serial_number   = row['serial_number'],
                        device_group    = row['device_group'],
                        site_id         = Site.objects.get(site_name=row['site_id']),
                        credentials     = Credentials.objects.get(username=row['credentials']),
                )

            # Redirect to the document upload after POST
            return HttpResponseRedirect(reverse('uploader.views.upload'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the upload page
    documents = Document.objects.all()

    # Render upload page with the documents and the form
    return render_to_response(
        'uploader/upload.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )

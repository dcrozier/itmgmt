from __future__ import unicode_literals
import django
from django.db import models
from uploader.models import Document
from datetime import datetime
import os


class RecentActions(models.Model):
    entry = models.CharField(max_length=200, blank=True, null=True)
    input_time = models.DateTimeField(default=django.utils.timezone.now)


class Credentials(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    description = models.CharField(max_length=200, primary_key=True, default="BLANK")
    community_string = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s' % self.username


def upload_path(filename):
    return os.sep.join(['template', Site.site_group, Site.site_name, str(datetime.now()) + '_' + filename])


class Site(models.Model):
    site_name = models.CharField(max_length=50)
    site_group = models.CharField(max_length=50, default="NO GROUP")
    site_credentials = models.ForeignKey(Credentials, blank=True, null=True)
    site_template = models.FileField(upload_to=upload_path, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.site_name


class Interface(models.Model):
    name = models.CharField(primary_key=True, max_length=25)
    index = models.IntegerField()
    vlan = models.IntegerField(default=1)
    speed = models.IntegerField(default=1000)
    description = models.CharField(max_length=50, blank=True, null=True)


class NetworkDevice(models.Model):
    device_name = models.CharField(max_length=80)
    device_type = models.CharField(max_length=50)
    ip_address = models.GenericIPAddressField(primary_key=True)
    port = models.IntegerField(default=22)
    data_vlan = models.IntegerField(default=1)
    voice_vlan = models.IntegerField(default=1)
    management_vlan = models.IntegerField(default=1)
    vendor = models.CharField(max_length=50, blank=True, null=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    os_version = models.CharField(max_length=100, blank=True, null=True)
    serial_number = models.CharField(max_length=50, blank=True, null=True)
    uptime_seconds = models.IntegerField(blank=True, null=True)
    device_group = models.CharField(max_length=50)
    last_scan = models.DateTimeField(blank=True, null=True)
    site_id = models.ForeignKey(Site)
    credentials = models.ForeignKey(Credentials, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.device_name + self.ip_address)


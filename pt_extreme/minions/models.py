from __future__ import unicode_literals

from django.db import models


class Minion(models.Model):
    mac_address = models.CharField(primary_key=True, max_length=17)
    public_ip = models.IPAddressField()
    private_ip = models.IPAddressField()
    host_name = models.CharField()

    def __unicode__(self):
        return self.host_name

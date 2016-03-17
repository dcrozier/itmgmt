"""pt_extreme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from uploader import views as uploader
from common import views as common

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', common.index, name='home'),
    url(r'^sites/$', common.site_view, name='site_view'),
    url(r'^sites/create_site/$', common.create_site, name='create_site'),
    url(r'^sites/create_site/add_credentials/', common.add_credentials, name='add_credentials'),
    url(r'^sites/create_site/add_site/', common.create_site, name='add_site'),
    url(r'^sites/view/(?P<site_name>[a-zA-Z0-9_]+)', common.detail, name='detail'),
    url(r'^upload/', uploader.upload, name='upload'),
]





"""juan URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url 
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from tastypie.api import Api
from juan.api import *


from main.views import index

entry_resource = InformationEntryResource()
receive_resource = ReceiveResource()
xbee_resource = XbeeEntryResource()
usuario_resource = UsuarioEntryResource()
empresa_resource = EmpresaEntryResource()

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(receive_resource.urls)),
    url(r'^api/', include(entry_resource.urls)),
    url(r'^api/', include(xbee_resource.urls)),
    url(r'^api/', include(usuario_resource.urls)),
    url(r'^api/', include(empresa_resource.urls)),
    url(r'^$', index),
] + staticfiles_urlpatterns()


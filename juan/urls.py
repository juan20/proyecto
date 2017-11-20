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
from jet.views import add_bookmark_view, remove_bookmark_view, toggle_application_pin_view, model_lookup_view



from main.views import index

modulo_resource = ModulosResource()
negocio_resource = NegocioResource()
area_resource = AreaResource()
estado_resource = EstadoResource()
recive_sensor_resource = ReceiveSensorResource()
recive_area_resource = ReceiveAreaResource()
recive_empleado_resource = ReceiveEmpleadoResource()
recive_hasempleado_resource = ReceiveHasEmpleadoResource()
recive_reloj_resource = ReceiveRelojResource()
recive_negocio_resource = ReceiveNegocioResource()
recive_credencial_resource = ReceiveCredencialResource()
recive_valores_resource = ReceiveValoresResource()
valor_entry_resource = ValorEntryResource()
crendial_check_resource = CredencialCheckResource()
valor_aentry_resource = ValorAEntryResource()
#negocio_total = NegocioTotal()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(modulo_resource.urls)),
    url(r'^api/', include(negocio_resource.urls)),
    url(r'^api/', include(area_resource.urls)),
    url(r'^api/', include(estado_resource.urls)),
    url(r'^api/', include(recive_sensor_resource.urls)),
    url(r'^api/', include(recive_area_resource.urls)),
    url(r'^api/', include(recive_empleado_resource.urls)),
    url(r'^api/', include(recive_hasempleado_resource.urls)),
    url(r'^api/', include(recive_reloj_resource.urls)),
    url(r'^api/', include(recive_negocio_resource.urls)),
    url(r'^api/', include(recive_credencial_resource.urls)),
    url(r'^api/', include(recive_valores_resource.urls)),
    url(r'^api/', include(valor_entry_resource.urls)),
    url(r'^api/', include(crendial_check_resource.urls)),
    url(r'^api/', include(valor_aentry_resource.urls)),
    #url(r'^api/', include(negocio_total.urls)),
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    url(r'^$', index),

] + staticfiles_urlpatterns()


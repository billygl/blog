from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^detalle/(?P<post_id>[0-9]+)$', views.detalle, name='detalle'),
]

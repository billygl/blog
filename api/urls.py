from django.conf.urls import url, include
from rest_framework import routers
from views import PostViewSet, UsuarioViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'usuario', UsuarioViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
    url(r'^rest-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

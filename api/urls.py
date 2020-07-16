from django.conf.urls import url, include
from rest_framework import routers
from api.views import UserViewSet

"""
The DefaultRouter class will define the standard REST(GET, POST, PUT, DELETE)
"""
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
]
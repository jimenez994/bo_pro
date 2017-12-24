from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^profile/(?P<id>\d+)$', views.profile),
]

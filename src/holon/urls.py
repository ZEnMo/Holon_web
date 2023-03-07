import imp

from django.urls import path

from holon.views.datamodel import DatamodelService
from holon.views.holon import HolonService, HolonV2Service
from holon.views.cloudclient import CloudclientService


urlpatterns = [path("holon/", HolonService.as_view())]

urlpatterns_v2 = [
    path("holon/", HolonV2Service.as_view()),
    path("datamodel/<int:pk>/", DatamodelService.as_view()),
    path("cloudclient/<int:pk>/", CloudclientService.as_view()),
]

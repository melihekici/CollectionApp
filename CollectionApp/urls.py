from django.conf.urls import url
from CollectionApp import views

urlpatterns = [
    url(r'^bins$', views.BinApi),
    url(r'^bins/([0-9]+)$', views.BinApi),

    url(r'^operations$', views.OperationApi),
    url(r'^operations/([0-9]+)$', views.OperationApi),

    url(r'^collections$', views.CollectionApi),
    url(r'^collections/([0-9]+)$', views.CollectionApi)
]
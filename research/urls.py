from django.conf.urls import url
from . import views

app_name = 'research'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^domain/(?P<pk>[0-9]+)/$', views.DomainView.as_view(), name='domain'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.ProjectView.as_view(), name='project')
]
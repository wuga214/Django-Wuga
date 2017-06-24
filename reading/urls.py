from django.conf.urls import url
from . import views

app_name = 'reading'

urlpatterns = [
    url(r'^$', views.indexview, name='index'),
    url(r'^category/(?P<selected_category>[\w]+)', views.filteredindexview, name='category')
]
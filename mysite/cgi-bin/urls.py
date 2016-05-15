from django.conf.urls import patterns, url
from lists import views

#urlpatterns = ['',
#    url(r'^$', views.index, name='index')
#]
urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)

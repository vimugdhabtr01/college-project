from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', 'composers_profile.views.show_list', name="show_list"),
    url(r'^create/$', 'composers_profile.views.create', name="create"),
    url(r'^edit/(?P<composer_id>\d+)/$', 'composers_profile.views.edit', name="edit"),
    url(r'^delete/(?P<composer_id>\d+)/$', 'composers_profile.views.delete', name="delete"),
    url(r'^show/(?P<composer_id>\d+)/$', 'composers_profile.views.show', name="show"),
    url(r'^pdf/$','composers_profile.views.Mypdf'),
]

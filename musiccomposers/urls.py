from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^composers_profile/', include('composers_profile.urls', namespace="composers_profile")),
    url(r'^$', 'composers_profile.views.home_page', name="home_page"),
    url(r'^forgotpassword/$', 'composers_profile.views.forgotpassword', name="forgotpassword"),
    url(r'^logout/$', 'composers_profile.views.logout_view', name="logout_view"),
    url(r'^resetpassword/(?P<token>\w+)/$', 'composers_profile.views.resetpassword', name="resetpassword"),
    url(r'^loginwithgoogle/$', 'composers_profile.views.loginwithgoogle', name="loginwithgoogle"),
    url(r'^loginwithgoogle/google/$','composers_profile.views.credentials', name="credentials")
)

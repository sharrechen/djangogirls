from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', 'trips.views.hello_world'),
    url(r'^$', 'trips.views.home'),
    url(r'^post/(?P<id>\d+)/$', 'trips.views.post_detail', name='post_detail'),
    url(r'^sign_up/', 'trips.views.sign_up'),
    url(r'^login', 'trips.views.login', name='login'),
    url(r'^logout', 'trips.views.logout', name='logout'),
)

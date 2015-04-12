from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', 'trips.views.hello_world'),
    url(r'^$', 'trips.views.home', name='home'),
    url(r'^about/$', 'trips.views.author', name='about'),
    url(r'^post/(?P<id>\d+)/$', 'trips.views.post_detail', name='post_detail'),
    url(r'^sign_up/', 'trips.views.sign_up'),
    url(r'^login', 'trips.views.login', name='login'),
    url(r'^logout', 'trips.views.logout', name='logout'),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
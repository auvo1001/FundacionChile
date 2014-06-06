from django.conf.urls import patterns, url
from management import views
from django.conf import settings

from management.views import OrgDetailView


urlpatterns = patterns('',

    url(r'^$', views.index, name='index'),
    url(r'^login/$',views.login_view,name='login'),
    url(r'^logout/$',views.logout_view,name='logout'),
    url(r'^dashboard/$',views.dashboard,name='dashboard'),
    url(r'^organization_create_form/$', views.create_organization, name='organization_create_form'),
    url(r'^organization/(?P<organization_name>\w+)/create_trip_form/$', views.create_trip, name='create_trip'),
    url(r'^search/$', views.search, name='search'),
    url(r'^organization/(?P<organization_name>\w+)/$', views.OrgDetailView, name='org_detail'),


   )


if settings.DEBUG:
        urlpatterns += patterns(
                'django.views.static',
                (r'media/(?P<path>.*)',
                'serve',
                {'document_root': settings.MEDIA_ROOT}), )

from django.conf.urls import patterns, url
from management import views
from django.conf import settings

from management.views import OrgDetailView


urlpatterns = patterns('',

    url(r'^$', views.index, name='index'),
    url(r'^login/$',views.login_view,name='login'),
    url(r'^logout/$',views.logout_view,name='logout'),
    url(r'^dashboard/$',views.dashboard,name='dashboard'),
    url(r'^create_organization_form/$', views.create_organization, name='create_organization_form'),
    url(r'^organization/(?P<organization_name_url>\w+)/create_trip_form/$', views.create_trip, name='create_trip_form'),
    url(r'^organization/(?P<organization_name_url>\w+)/create_rep_form/$', views.create_rep, name='create_rep_form'),
    url(r'^search/$', views.search, name='search'),
    url(r'^organization/(?P<organization_name_url>\w+)/$', views.OrgDetailView, name='org_detail'),
    url(r'^organization/(?P<organization_name_url>\w+)/edit/$', views.edit_organization, {}, 'edit_organization'),

   )


if settings.DEBUG:
        urlpatterns += patterns(
                'django.views.static',
                (r'media/(?P<path>.*)',
                'serve',
                {'document_root': settings.MEDIA_ROOT}), )

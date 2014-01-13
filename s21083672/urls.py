from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

import os.path
site_media = os.path.join(
    os.path.dirname(__file__), "../", "myApp", "static", 'site_media'
)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 's21083672.views.home', name='home'),
    # url(r'^s21083672/', include('s21083672.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    #url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
    #{ 'document_root': site_media, "show_indexes": True }),

    url(r'^$', 'myApp.views.home', name='home'),
)

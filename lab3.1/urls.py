from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'pages.views.home'),
    url(r'^log/(?P<temp>([-,.\w]*/)*)$','pages.views.listing'),
    url(r'^library/(?P<sub>(books){0,1}?)$', 'library.views.books'),
    url(r'^library/books/(?P<sub>\d+?)/$', 'library.views.book'),
    #url(r'^library/authors/?$', 'library.views.authors'),
    #url(r'^library/authors/(?P<sub>\d+?)/$', 'library.views.author'),

    # url(r'^control_panel/', include('control_panel.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)

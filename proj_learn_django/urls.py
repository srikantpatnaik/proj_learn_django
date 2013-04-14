from django.conf.urls import patterns, include, url
#added by srikant
from app_add.views import app_add
from app_add_database.views import app_add_database
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^add/$',app_add),
    url(r'^add-database/$',app_add_database),
    # Examples:
    # url(r'^$', 'learn_django.views.home', name='home'),
    # url(r'^learn_django/', include('learn_django.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

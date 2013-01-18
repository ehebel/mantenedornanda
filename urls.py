from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from mantnandaapp import views
import modeladorcie9.views


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mantenedornanda.views.home', name='home'),
    # url(r'^mantenedornanda/', include('mantenedornanda.foo.urls')),
    (r'^$', views.lista_nandas),
    (r'^lista_nandas/(\d{1,4})/$',views.selec_nanda),
    (r'^procedimientos/', modeladorcie9.views.list_cas_proc),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

# Uncomment these two lines to enable your static files on PythonAnywhere
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()


from django.conf.urls import patterns, include, url
from orders.views import view_total
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'menu_orders.views.home', name='home'),
    url(r'^orders/', include('orders.urls', namespace='orders')),
    url(r'^export/', view_total, name='total_cost'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
)

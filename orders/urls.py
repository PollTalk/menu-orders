from django.conf.urls import patterns, include, url
# from orders.views import OrdersView
from orders import views
urlpatterns = patterns('',
            url(r'^$', views.create_orders, name='create-orders'),
            url(r'^hello/$', views.pdf_handler, name='pdf-handler'),
           )
from django.conf.urls import patterns, include, url
# from orders.views import OrdersView
from orders import views
urlpatterns = patterns('',
            url(r'^$', views.index, name='index'),
            url(r'^login$', views.login_user, name='login'),
            url(r'^logout$', views.logout_user, name='logout_user'),
            url(r'^create-order', views.create_orders, name='create_orders'),
            url(r'^hello/$', views.pdf_handler, name='pdf-handler'),
           )
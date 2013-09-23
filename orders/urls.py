from django.conf.urls import patterns, include, url
from orders import views
urlpatterns = patterns('',
            url(r'^$', views.create_orders, name='create-orders'),
)
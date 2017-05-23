from django.conf.urls import url

app_name='blog'
from . import views

urlpatterns=[url(r'^$',views.blogtest, name='blogtest'),
             url(r'^get_form/$', views.get_form, name='get_form')]
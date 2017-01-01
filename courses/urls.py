from django.conf.urls import url
from django.conf.urls import url, include

from . import views

urlpatterns = [
  url(r'^$', views.course_list),
  url(r'(?P<course_pk>\d+)/(?P<step_pk>\d+)/$', views.step_detail, 
      name='step'),
  url(r'(?P<pk>\d+)/$', views.course_detail, 
      name='detail'),
]
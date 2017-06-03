from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.UserDetailAPIView.as_view(), name='list'),
    url(r'^login/$', views.UserLoginAPIView.as_view(), name='login'),
    url(r'^register/$', views.UserCreateAPIView.as_view(), name='register'),
    url(r'^movie/$', views.MovieListAPIView.as_view(), name='movie'),

]

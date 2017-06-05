from django.conf.urls import url, include
from rest_framework import routers
from . import views
#from rest_framework.schemas import get_schema_view

# DefaultRouter class automatically creates the API root view for us
router = routers.DefaultRouter()
router.register(r'movies', views.MovieListAPIView)

#schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    url(r'^list/$', views.UserDetailAPIView.as_view(), name='list'),
    url(r'^login/$', views.UserLoginAPIView.as_view(), name='login'),
    url(r'^register/$', views.UserCreateAPIView.as_view(), name='register'),
    url(r'^', include(router.urls)),

]

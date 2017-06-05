from django.conf.urls import url, include
from rest_framework import routers
from movie import views

# DefaultRouter class automatically creates the API root view for us
router = routers.DefaultRouter()
router.register(r'movie', views.MovieListViewSet)


urlpatterns = [
	url(r'^', include(router.urls)),
    url(r'^user/$', views.UserDetailAPIView.as_view(), name='user'),
    url(r'^login/$', views.UserLoginAPIView.as_view(), name='login'),
    url(r'^register/$', views.UserCreateAPIView.as_view(), name='register'),

]

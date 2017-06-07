from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from movie import views

# DefaultRouter class automatically creates the API root view for us
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'movie', views.MovieViewSet)
router.register(r'comment', views.CommentViewSet)
router.register(r'order', views.OrderViewSet)


urlpatterns = [
	url(r'^', include(router.urls)),
	url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
 	url(r'^register/$', views.UserCreateAPI.as_view()),
 	url(r'^login/$', views.UserLoginAPIView.as_view()),
]


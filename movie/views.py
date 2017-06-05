from .serializers import UserCreateSerializer, UserLoginSerializer, UserDetailSerializer, MovieListSerializer, CommentSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from django.contrib.auth.models import User
from movie.models import Movie, Comment

class MovieListViewSet(viewsets.ModelViewSet):
	#provides 'list' 'create' 'retrieve' 'update' 'destroy'
	queryset = Movie.objects.all()
	serializer_class = MovieListSerializer
	permission_classes = [AllowAny]

class CommentViewSet(viewsets.ModelViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
	permission_classes = [AllowAny]
	

class UserDetailAPIView(ListAPIView):
	serializer_class = UserDetailSerializer
	queryset = User.objects.all()
	permission_classes = [AllowAny]

class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer
	queryset = User.objects.all()
	permission_classes = [AllowAny]

class UserLoginAPIView(APIView):
	permission_classes = [AllowAny]
	serializer_class = UserLoginSerializer

	def post(self, request, *args, **kwargs):
		data = request.data
		serializer = UserLoginSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			new_data = serializer.data
			return Response(new_data, status=HTTP_200_OK)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


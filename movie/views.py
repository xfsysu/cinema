from .serializers import MovieSerializer, CommentSerializer, UserSerializer, OrderSerializer
from rest_framework import viewsets
from movie.models import Movie, Comment, Order
from django.contrib.auth.models import User

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer



class MovieViewSet(viewsets.ModelViewSet):
	#provides 'list' 'create' 'retrieve' 'update' 'destroy'
	queryset = Movie.objects.all()
	serializer_class = MovieSerializer



class CommentViewSet(viewsets.ModelViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)


class OrderViewSet(viewsets.ModelViewSet):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)


from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from .serializers import UserCreateSerializer, UserLoginSerializer
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response

User = get_user_model()

class UserCreateAPI(CreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserCreateSerializer


class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer
    
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
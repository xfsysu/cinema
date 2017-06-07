from movie.models import Movie, Comment, Order
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
	orders = serializers.HyperlinkedRelatedField(many=True, view_name='order-detail', read_only=True)
	comments = serializers.HyperlinkedRelatedField(many=True, view_name='comment-detail', read_only=True)
	class Meta:
		model = User
		fields = ('url', 'id', 'username', 'email', 'password', 'orders', 'comments')



class MovieSerializer(serializers.ModelSerializer):
	comment = serializers.HyperlinkedRelatedField(many=True, view_name='comment-detail', read_only=True)
	class Meta:
		model = Movie
		fields = ('url', 'id', 'mName', 'director', 'performer', 'duration', 'score', 'brief', 'price', 'image_urls', 'comment')



class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = ('url', 'id', 'content', 'created_time', 'movie', 'user')
		

class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = ('url', 'id', 'created_time', 'price', 'isPay', 'movie', 'user')


from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()

class UserCreateSerializer(serializers.ModelSerializer):
	email = serializers.EmailField(label='email')
	password = serializers.CharField(label='password')
	password2 = serializers.CharField(label='Confirm password')

	class Meta:
		model = User
		fields = ('username', 'email', 'password', 'password2')
		extra_kwargs = {'password': {'write_only': True}, 'password2': {'write_only': True}}


	def validate_username(self, value):
		data = self.get_initial()
		username = data.get('username')
		user_qs = User.objects.filter(username=username)
		if user_qs.exists():
			raise serializers.ValidationError("This username has already registered.")
		return value

	def validate_email(self, value):
		data = self.get_initial()
		email = data.get('email')
		user_qs = User.objects.filter(email=email)
		if user_qs.exists():
			raise serializers.ValidationError("This email has already registered.")
		return value

	def validate_password(self, value):
		data = self.get_initial()
		password1 = data.get('password2')
		password2 = value

		if password1 != password2:
			raise serializers.ValidationError("password must match.")
		return value

	def create(self, validate_data):
		username = validate_data['username']
		email = validate_data['email']
		password = validate_data['password']
		user_obj = User(username=username, email=email)
		user_obj.set_password(password)
		user_obj.save()
		return validate_data

class UserLoginSerializer(serializers.ModelSerializer):
	token = serializers.CharField(allow_blank=True, read_only=True)
	username = serializers.CharField(required=False, allow_blank=True)
	password = serializers.CharField(required=False, allow_blank=True)
	email = serializers.EmailField(required=False, allow_blank=True)

	class Meta:
		model = User
		fields = ('username', 'email', 'password', 'token')
		extra_kwargs = {'password': {'write_only': True }}

	def validate(self, data):
		user_obj = None
		username = data.get('username', None)
		email = data.get('email', None)
		password = data['password']

		if not email and not username:
			raise serializers.ValidationError('A username or email is required to login.')

		user = User.objects.filter(
			Q(email=email) |
			Q(username=username)
		).distinct()
		user = user.exclude(email__isnull=True).exclude(email__iexact='')
		print (user)
		if user.exists() and user.count() == 1:
			user_obj = user.first()
		else:
			raise serializers.ValidationError("This username/email is not valid.")

		if user_obj:
			if not user_obj.check_password(password):
				raise serializers.ValidationError("Incorrect password. please try again.")

		data['token'] = "SOME RANDOM TOKEN"
		return data
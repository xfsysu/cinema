from django.contrib.contenttypes.models import ContentType
from rest_framework.serializers import ModelSerializer, CharField, EmailField, ValidationError, HyperlinkedModelSerializer
from django.contrib.auth.models import User
from movie.models import Movie

class MovieListSerializer(HyperlinkedModelSerializer):
	class Meta:
		model = Movie
		fields = ('title', 'score', 'quote', 'image_urls')

class UserDetailSerializer(ModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name',]


class UserCreateSerializer(ModelSerializer):
	password = CharField()
	password2 = CharField(label='Confirm password')

	class Meta:
		model = User
		fields = ['username', 'email', 'password', 'password2']


	def validate_password(self, value):
		data = self.get_initial()
		email = data.get('email')
		password1 = data.get("password2")
		password2 = value
		if password1 != password2:
			raise ValidationError("Password must match.")

		user_qs = User.objects.filter(email=email)
		if user_qs.exists():
			raise ValidationError("This Email has already registered.")
		return value

	def validate_password2(self, value):
		data = self.get_initial()
		password1 = data.get("password")
		password2 = value
		if password1 != password2:
			raise ValidationError("Password must Match.")
		return value

	def create(self, validate_data):
		username = validate_data['username']
		email = validate_data['email']
		password = validate_data['password']
		user_obj = User(username=username, email=email)
		user_obj.set_password(password)
		user_obj.save()
		return validate_data


class UserLoginSerializer(ModelSerializer):
	token = CharField(allow_blank=True, read_only=True)
	username = CharField()
	email = EmailField(label='Email Address')

	class Meta:
		model = User
		fields = ['username', 'email', 'password', 'token']

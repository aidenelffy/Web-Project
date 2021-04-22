from rest_framework import serializers
from .models import Post, Product,Furniture,Order
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'img', 'category')



class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'title', 'body', 'price', 'img')


class FurnitureSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Furniture
        fields = ('id', 'title', 'body', 'price', 'img', 'img2', 'img3', 'body2', 'img4', 'body3','product')



# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

#Cart
class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True, default=1)

    class Meta:
        model = Order
        fields = '__all__'
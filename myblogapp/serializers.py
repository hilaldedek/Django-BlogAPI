from .models import Post,Category
from rest_framework import serializers



class PostSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField()
    user_id=serializers.IntegerField()

    class Meta:
        model= Post
        exclude=['created_date']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

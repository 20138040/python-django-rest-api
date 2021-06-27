# from django.db.models import fields
from typing import Union
from rest_framework import fields, serializers
from .models import Article


# class ArticleSerializer(serializers.Serializer):
#     created = serializers.DateTimeField()
#     title = serializers.CharField(max_length=100)
#     author = serializers.CharField(max_length=100)
#     email = serializers.EmailField()

#     def create(self, validated_data):
#         return Article.objects.create(validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.author = validated_data.get('author', instance.author)
#         instance.email = validated_data.get('email', instance.email)
#         instance.created = validated_data.get('created', instance.created)
        
#         instance.save()
#         return instance
        

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields = ['id', 'title', 'author', 'email']
        fields = '__all__'
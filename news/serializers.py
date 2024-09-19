from rest_framework import serializers
from .models import NewsArticle

class NewsArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsArticle
        fields = ['id', 'title', 'content', 'category', 'published_date', 'image']
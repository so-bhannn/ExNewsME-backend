from rest_framework.response import Response
from rest_framework.views import APIView
from .models import NewsArticle
from .serializers import NewsArticleSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .permissions import IsNewsArticleOwner
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

class NewsArticleListView(APIView):
    queryset = NewsArticle.objects.all()
    serializer_class = NewsArticleSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['title', 'author', 'category']
    ordering_fields = ['title', 'created_at']
    ordering = ['created_at']
    pagination_class = LimitOffsetPagination
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        news_articles = self.queryset
        title = request.query_params.get('title')
        author = request.query_params.get('author')
        category = request.query_params.get('category')

        if title:
            news_articles = news_articles.filter(title__icontains=title)
        if author:
            news_articles = news_articles.filter(author__icontains=author)
        if category:
            news_articles = news_articles.filter(category__icontains=category)

        paginator = self.pagination_class()
        paginated_news_articles = paginator.paginate_queryset(news_articles, request)
        serializer = self.serializer_class(paginated_news_articles, many=True)
        return paginator.get_paginated_response(serializer.data)
class NewsArticleDetailView(APIView):
    def get(self, request, pk):
        news_article = NewsArticle.objects.get(pk=pk)
        serializer = NewsArticleSerializer(news_article)
        return Response(serializer.data)

class NewsArticleCreateView(APIView):
    def post(self, request):
        image = request.FILES.get('image')
        if image:
            request.data['image'] = image
        serializer = NewsArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class NewsArticleUpdateView(APIView):
    permission_classes = [IsNewsArticleOwner]

    def put(self, request, pk):
        news_article = NewsArticle.objects.get(pk=pk)
        image = request.FILES.get('image')
        if image:
            request.data['image'] = image
        serializer = NewsArticleSerializer(news_article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class NewsArticleDeleteView(APIView):
    def delete(self, request, pk):
        news_article = NewsArticle.objects.get(pk=pk)
        news_article.delete()
        return Response(status=204)

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
        })

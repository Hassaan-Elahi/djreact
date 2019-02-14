from rest_framework import generics
from articles.models import Article
from .serializers import ArticlesSerializer


class ArticlesListView(generics.ListAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticlesSerializer


class ArticlesDetailView(generics.RetrieveAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticlesSerializer
	
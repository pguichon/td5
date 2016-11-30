from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from api.models import Post
from api.serializers import PostSerializer


class PostView(viewsets.ModelViewSet):
    """
    Post du blog
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

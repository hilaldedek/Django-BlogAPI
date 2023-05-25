from rest_framework.viewsets import ModelViewSet
from .serializers import Post,PostSerializer

class PostViews(ModelViewSet):
    queryset=Post.objects.all().order_by('-id')
    serializer_class=PostSerializer

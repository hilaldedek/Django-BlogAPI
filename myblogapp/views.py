from rest_framework.viewsets import ModelViewSet
from .serializers import Post,PostSerializer,Category,CategorySerializer

class PostViews(ModelViewSet):
    queryset=Post.objects.all().order_by('-id')
    serializer_class=PostSerializer

class CategoryViews(ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
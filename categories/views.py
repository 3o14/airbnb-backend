from rest_framework.viewsets import ModelViewSet
from .models import Category
from .serializers import CategorySerializer

# 인자로 APIView를 받는다
class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
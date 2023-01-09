from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        
        # fields = 어떤 필드를 보이게 할지 설정
        # 모든 필드 보이게 하기
        fields = "__all__" 
        
        # 제외시킬 필드 고르기
        exclude = (
            "created_at",
        )
        
        # 포함시킬 필드 고르기
        include = (
            "name",
            "kind",
        )
from rest_framework.serializers import ModelSerializer
from .models import Amenity, Room
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer
class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = (
            "name",
            "description",
        )

# room 하나 자세히 보는 serializer
class RoomDetailSerializer(ModelSerializer):

    # 장고가 owner, category, amenities를 serialize하려고 할때
    # 보여주고 싶은 부분을 지정한 커스텀한 serializer를 사용하라고 알려주는 코드
    owner = TinyUserSerializer(read_only=True)
    amenities = AmenitySerializer(
        read_only=True,
        many=True,
    )
    category = CategorySerializer(
        read_only=True,
    )
    class Meta:
        model = Room
        fields = "__all__"
        # room의 owner, amenities 등의 정보를 id가 아닌 object로 표시하기 위한 코드
        depth = 1

# 여러 room 한꺼번에 보는 serializer
class RoomListSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = (
            "pk",
            "name",
            "country",
            "city",
            "price",
        )

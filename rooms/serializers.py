from rest_framework import serializers
from .models import Amenity, Room
from users.serializers import TinyUserSerializer
from reviews.serializers import ReviewSerializer
from categories.serializers import CategorySerializer


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = (
            "name",
            "description",
        )

# room 하나 자세히 보는 serializer
class RoomDetailSerializer(serializers.ModelSerializer):

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
    
    rating = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = "__all__"
        # room의 owner, amenities 등의 정보를 id가 아닌 object로 표시하기 위한 코드
        
    # 평균점수(rating)을 구하는 메소드
    # get_ 형식이어야 함
    def get_rating(self, room):
        return room.rating()
    
    def get_is_owner(self, room):
        # serializer에 설정해둔 context로 request값 가져오기
        request = self.context["request"]
        return room.owner == request.user


class RoomListSerializer(serializers.ModelSerializer):

    rating = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()
    class Meta:
        model = Room
        fields = (
            "pk",
            "name",
            "country",
            "city",
            "price",
            "rating",
            "is_owner",
        )

    def get_rating(self, room):
        return room.rating()

    def get_is_owner(self, room):
        request = self.context["request"]
        return room.owner == request.user
from rest_framework.serializers import ModelSerializer
from rooms.serializers import RoomListSerializer
from .models import Wishlist
# room의 정보를 사용하기 위해 rooms의 시리얼라이저를 가져온다
# Wishlist의 시리얼라이저를 만들기 위해 Wishlist 모델을 가져옴

class WishlistSerializer(ModelSerializer):

    # rooms의 복수정보, 읽기허용 옵션으로 가져온다
    rooms = RoomListSerializer(
        many=True,
        read_only=True,
    )

    # 위시리스트 시리얼라이저 설정
    class Meta:
        model = Wishlist
        fields = (
            "pk",
            "name",
            "rooms",
        )
from django.db import models
from common.models import CommonModel

class Photo(CommonModel):
    
    file = models.ImageField()
    description = models.CharField(max_length=140,)
    room = models.ForeignKey(
        "rooms.Room",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    
    def __str__(self):
        return "Photo File"
    
class Video(CommonModel):
    
    file = models.FileField()
    
    # 활동 당 하나의 영상만 가질 수 있도록 일대일 관계 설정
    experience = models.OneToOneField(
        "experiences.Experience",
        on_delete=models.CASCADE,
    )
    
    def __str__(self):
        return "Video File"
from django.db import models

class House(models.Model):
    
    """Model Definition for Houses""" # 모델을 만들때 관례적으로 적는 것(모델에 대한 설명)
    
    name = models.CharField(max_length=140) # 적당한 길이를 가진 문자열
    price_per_night = models.PositiveIntegerField(
        verbose_name="Price",
        help_text="Positive Numbers Only",
        ) # 양의 정수
    description = models.TextField() # 긴 길이를 가진 문자열
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(
        verbose_name="Pets allowed?",
        default=True,
        help_text="Does this house allow pets?",
        )
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)
    # 외래키로 사용자의 ID인 PK가져오기 | models.ForeignKey("참조할 model", on_delete=)
    # on_delete는 이 컬럼의 정보가 없어졌을때의 행동을 정함
    # -> on_delete=models.SET_NULL : 사용자가 계정을 삭제해도 house는 주인이 없는 상태로 남음
    # -> on_delete=models.CASCADE : 사용자가 계정을 삭제하면 house도 지워짐
    
    def __str__(self):
        return self.name
    
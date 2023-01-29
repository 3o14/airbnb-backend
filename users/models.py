from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # gender 컬럼에 옵션으로 넣어 줄 클래스
    class GenderChoices(models.TextChoices):
        # 첫번째 값은 데이터베이스에 들어갈 value, 두번째 값은 관리자 페이지에 들어갈 label
        MALE = ("male", "Male") 
        FEMALE = ("female", "Female")
        
    class LanguageChoices(models.TextChoices):
        KR = ("kr", "Korea")
        EN = ("en", "English")
        
    class CurrencyChoices(models.TextChoices):
        WON = "won", "Korean Won"
        USD = "usd", "Dollar"
    # 성과 이름으로 분류하는 것은 서구적인 정보 입력 방식이기 때문에 관리자 페이지에서 보이지 않도록 설정한다. editable=False
    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)
    
    # 사용자 프로필사진 -> ImageField()를 쓰려면 Pillow 가 설치되어 있어야 함
    # blank=True: 필드가 필수사항이 아니게 설정
    avatar = models.URLField(blank=True)
    # 이름 입력창
    name = models.CharField(max_length=150, default="")
    # 유저가 호스트일 경우
    is_host = models.BooleanField(default=False)
    
    gender = models.CharField(max_length=10, choices=GenderChoices.choices,)
    language = models.CharField(max_length=2, choices=LanguageChoices.choices,)
    currency = models.CharField(max_length=5, choices=CurrencyChoices.choices,)
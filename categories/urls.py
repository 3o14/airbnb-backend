from django.urls import path
from . import views

urlpatterns = [
    # 클래스로 수정했기 때문에
    # 클래스를 호출한 뒤 as_view()를 호출해야 한다. (그냥 규칙임)
    path("", views.Categories.as_view()),
    path("<int:pk>", views.CategoryDetail.as_view()),
]
from django.urls import path,re_path
from . import views # 从自己的 app 目录引入 views
urlpatterns = [
    path('index/', views.index),
]

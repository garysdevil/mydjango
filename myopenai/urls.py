from django.urls import path, re_path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('chat/<str:prompt>/', views.chat, name='openai_chat'),
    # url(r'^otherattr/$', views.other_attr),
]
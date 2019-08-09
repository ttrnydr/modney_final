from .views import *
from django.urls import path

app_name='freeboard'
urlpatterns=[
    path('', BoardLV.as_view(), name='board'),
    path('<int:pk>/', BoardDV.as_view(), name='board_detail'),
    path('freeboard/add/',BoardCreateView.as_view(), name="board_add"),
    path('freeboard/change/',BoardChangeLV.as_view(), name="board_change"),
    path('freeboard/<int:pk>/update/',BoardUpdateView.as_view(), name="board_update"),
    path('freeboard/<int:pk>/delete/', BoardDeleteView.as_view(), name="board_delete"),
]
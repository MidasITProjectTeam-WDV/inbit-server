from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from .views import (
    GetRoomAPI,
    ListRoomAPI,
    RoomAdminViewSet,
)
router = routers.DefaultRouter()
router.register(r"roomadmin",RoomAdminViewSet,basename="roomadmin")

urlpatterns = [
    path('', include(router.urls)),
    path("",ListRoomAPI.as_view()),
    path("<pk>", GetRoomAPI.as_view()),
]
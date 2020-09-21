from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import (
    GetRoomAPI,
    ListRoomAPI,
    RoomAdminViewSet,
)

router = DefaultRouter()
router.register(r"roomadmin",RoomAdminViewSet,basename="roomadmin")

urlpatterns = [
    path("",ListRoomAPI.as_view()),
    path("<pk>", GetRoomAPI.as_view()),
    path("", include(router.urls)),
]
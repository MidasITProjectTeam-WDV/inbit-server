from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from .views import (
    CreateQueueAPI,
    ListReservationAPI,
    AdminQueueAPI,
    AdminReservationAPI
)
router = routers.DefaultRouter()
router.register(r"queueadmin",AdminQueueAPI,basename="roomqueue")
router.register(r"roomadmin",AdminQueueAPI,basename="roomreserve")


urlpatterns = [
    path('', include(router.urls)),
    path("reserve/",CreateQueueAPI.as_view()),
    path("reserve/", ListReservationAPI.as_view()),
]
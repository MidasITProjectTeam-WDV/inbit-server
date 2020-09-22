from rest_framework import routers
from django.urls import path,include

from .views import (
    QueueViewSet,
    AdminQueueAPI,
    AdminReservationAPI
)

router = routers.DefaultRouter()
router.register(r"queueadmin",AdminQueueAPI,basename="queueadmin")
router.register(r"reserveadmin",AdminQueueAPI,basename="reserveadmin")
router.register(r"queue",QueueViewSet,basename="queue")

urlpatterns = [
    path('', include(router.urls)),
]
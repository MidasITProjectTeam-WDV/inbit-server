from rest_framework import serializers
from .models import Reservation,Reservation_queue


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"


class QueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation_queue
        fields = "__all__"

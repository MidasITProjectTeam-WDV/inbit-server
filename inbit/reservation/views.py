from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,mixins,viewsets

from .models import Reservation,Reservation_queue
from .serializers import ReservationSerializer, QueueSerializer
# Create your views here.

class QueueViewSet(viewsets.ViewSet):
    #인증검사

    def create(self,request):
        request.data["email"] = reqeust.user.email
        serializer = Reservation_queue(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors)

        serializer.save()
        return Response(serializer.data)


    def list(self, request):

        queryset = Reservation_queue.objects.filter(email=request.user.email)
        serializer = QueueSerializer(queryset, many=True)

        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

class GETReservationAPI(mixins.RetrieveModelMixin):

    def retrieve(self, request, *args, **kwargs):
        room_queryset = Reservation.objects.get(room_id=self.kwargs["room_id"])
        first_queryset = list(room_queryset.objects.filter(period=10))
        second_queryset = list(room_queryset.objects.filter(period=11))
        
        data = [
            {
                "period":10,
                "people": len(first_queryset)
            },
            {
                "period":11,
                "people": len(second_queryset)
            }
        ]

        return Response(data)

        



class AdminQueueAPI(viewsets.ModelViewSet):
    serializer_class = QueueSerializer
    queryset = Reservation_queue.objects.all()

    #email -> self.request.user.email 로 바꿀것
    def post(self,request,*arg,**kwargs):
        request.data["email"] = "email"
        return super().post(request,*arg,**kwargs)
    


class AdminReservationAPI(viewsets.ModelViewSet):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()
    
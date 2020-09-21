from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from .models import Reservation,Reservation_queue
from .serializers import ReservationSerializer, QueueSerializer
# Create your views here.

class CreateQueueAPI(generics.CreatedAPIView):

    #인증검사
    serializer_class = QueueSerializer

    def post(self, request, *arg, **kwargs):
        request.data["email"] = self.request.user.email
        return super().post(request,*args,**kwargs)
        

class GetReservationAPI(generics.RetrieveAPIView):

    #인증검사
    serializer_class = ReservationSerializer

    def get(self,request,*arg,**kwargs):
        return super().get(request,*arg,**kwargs)

    def get_object(self):
        obj = Reservation.object.get(id=self.kwargs["id"])
        return obj
    

class AdminQueueAPI(generics.RetrieveUpdateDestroyAPIView):

    #인증검사
    serializer_class = QueueSerializer


class AdminReservationAPI(generics.)
    
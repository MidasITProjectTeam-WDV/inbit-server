from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,mixins,viewsets

from .models import Reservation,Reservation_queue
from .serializers import ReservationSerializer, QueueSerializer
# Create your views here.

class CreateQueueAPI(generics.CreatedAPIView):

    #인증검사
    serializer_class = QueueSerializer

    #email -> self.request.user.email 로 바꿀것
    def post(self, request, *arg, **kwargs):
        request.data["email"] = "email"
        return super().post(request,*args,**kwargs)
        

    
class ListReservationAPI(generics.ListAPIView):

    serializer_class = ReservationSerializer

    def get(self,request,*arg,**kwargs):
        return super().get(request,*arg,**kwargs)

    def get_queryset(self):
        return Reservation.objects.all()
    

class AdminQueueAPI(viewsets.ModelViewSet):
    serializer_class = QueueSerializer
    queryset = Reservation_queue.objects.all()

    #email -> self.request.user.email 로 바꿀것
    def post(self,request,*arg,**kwargs):
        request.data["email"] = "email"
        return super().post(reqeust,*args,**kwargs)
    


class AdminReservationAPI(generics.Model):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()
    
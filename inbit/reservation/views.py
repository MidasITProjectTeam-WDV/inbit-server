from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,mixins,viewsets
from .models import Reservation,Reservation_queue
from .serializers import ReservationSerializer, QueueSerializer
from rest_framework.permissions import IsAuthenticated
from user.permissions import IsAdmin
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.decorators import action

import datetime
# Create your views here.

class QueueViewSet(viewsets.ViewSet):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]

    def create(self,request):
        request.data["email"] = request.user.email
        serializer = Reservation_queue(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors)

        serializer.save()
        return Response(serializer.data)


    def list(self, request):
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        queryset = Reservation_queue.objects.filter(email=request.user.email).filter(date=today)
        serializer = QueueSerializer(queryset, many=True)

        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def destroy(self, request, pk=None):
        pass

class GETReservationAPI(generics.GenericAPIView,mixins.RetrieveModelMixin):

    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]

    def retrieve(self, request, *args, **kwargs):
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        room_queryset = Reservation.objects.get(room_id=self.kwargs["room_id"]).filter(date=today)
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

    permission_classes = [IsAuthenticated & IsAdmin]
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = QueueSerializer
    queryset = Reservation_queue.objects.all()

    def list(self, request):
        queryset = Reservation_queue.objects.filter(is_active=True)
        serializer = QueueSerializer(queryset, many=True)

        return Response(serializer.data)
    
    def post(self,request,*args,**kwargs):
        request.data["email"] = self.request.user.email
        return super().post(request,*args,**kwargs)

    
    @action(detail=True,methods=['PATCH'])
    def accept(self,request,*args,**kwargs):  
        kwargs['partial'] = True
        obj = Reservation_queue.objects.filter(pk=kwargs["pk"])
        data = {
            "room_id":obj["room_id"],
            "email":obj["email"],
            "period":obj["period"]
        }
        serializer = ReservationSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors)

        serializer.save()

        return self.update(request, *args, **kwargs)
        

    @action(detail=True,methods=['PATCH'])
    def refuse(self,request,*args,**kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
 
    


class AdminReservationAPI(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & IsAdmin]
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()
    
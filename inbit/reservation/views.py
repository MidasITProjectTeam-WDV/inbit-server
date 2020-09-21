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

class ReservationViewSet(viewsets.ViewSet):
    

        



class AdminQueueAPI(viewsets.ModelViewSet):
    serializer_class = QueueSerializer
    queryset = Reservation_queue.objects.all()

    #email -> self.request.user.email 로 바꿀것
    def post(self,request,*arg,**kwargs):
        request.data["email"] = "email"
        return super().post(request,*arg,**kwargs)
    


class AdminReservationAPI(generics.Model):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()
    
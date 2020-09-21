from django.shortcuts import render
from rest_framework import generics,mixins,viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Room
from .serializers import RoomSerializer

# Create your views here.
class GetRoomAPI(generics.RetrieveAPIView):
    serializer_class = RoomSerializer
    
    def get(self, request , *args , **kwargs):
        return super().get( request , *args , **kwargs)
    
    def get_queryset(self):
        return Room.objects.get(id=self.kwargs["pk"])
    
class ListRoomAPI(generics.ListAPIView):
    serializer_class = RoomSerializer

    def get(self, request , *args , **kwargs):
        return super().get( request , *args , **kwargs)

    def get_queryset(self):
        return Room.objects.all()
    
    

class RoomAdminViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
 

    


        




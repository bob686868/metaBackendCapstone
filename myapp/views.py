from django.shortcuts import render
from rest_framework import generics,viewsets
from django.db import models
from .serializers import MenuSerializer,BookingSerializer
from .models import Menu,Booking
from rest_framework.permissions import IsAuthenticated
# Create your views here.
def index(request):
     return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
     permission_classes = [IsAuthenticated]
     queryset=Menu.objects.all()
     serializer_class=MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
     queryset=Menu.objects.all()
     serializer_class=MenuSerializer
     permission_classes = [IsAuthenticated] 
class BookingViewSet(viewsets.ModelViewSet):
     queryset=Booking.objects.all()
     serializer_class=BookingSerializer
     permission_classes = [IsAuthenticated] 
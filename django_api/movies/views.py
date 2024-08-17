from django.shortcuts import render
# add in order to make the Rest Api works
from rest_framework import viewsets
from .serializers import MoviedataSerializer
from .models import Moviedata
# Create your views here.

# creating  a class based view:

class MovieViewset (viewsets.ModelViewSet):
    queryset = Moviedata.objects.all()
    serializer_class = MoviedataSerializer

# class based view for action movie

class ActionViewSet (viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ='action')
    serializer_class = MoviedataSerializer


class ComedyViewSet (viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ='comedy')
    serializer_class = MoviedataSerializer

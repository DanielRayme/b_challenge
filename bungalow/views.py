from django.shortcuts import render

# Create your views here.
from .models import PropertyModel
from rest_framework import viewsets
from .serializers import PropertySerializer


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = PropertyModel.objects.all().order_by('zillow_id')
    serializer_class = PropertySerializer



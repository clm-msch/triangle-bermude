from re import search
from turtle import title

from rest_framework import filters, viewsets

from .models import (Access_type, Adresse, Audience, Event, Group, Occurrence,
                     Price_type, Tag)
from .serializers import (Access_typeSerializer, AdresseSerializer,
                          AudienceSerializer, EventSerializer, GroupSerializer,
                          OccurenceSerializer, Price_typeSerializer,
                          TagSerializer)


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'tags', 'pmr', 'blind', 'deaf']
    ordering_fields = ['title', 'date_end']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.query_params.get('title')
        tags = self.request.query_params.get('tags')
        pmr = self.request.query_params.get('pmr')
        blind = self.request.query_params.get('blind')
        deaf = self.request.query_params.get('deaf')
        if title is not None:
            queryset = queryset.filter(title=title)
        elif tags is not None:
            queryset = queryset.filter(tags=tags)
        elif pmr is not None:
            queryset = queryset.filter(pmr=pmr)
        elif blind is not None:
            queryset = queryset.filter(blind=blind)
        elif deaf is not None:
            queryset = queryset.filter(deaf=deaf)
        return queryset

class OccurrenceViewSet(viewsets.ModelViewSet):
    queryset = Occurrence.objects.all()
    serializer_class = OccurenceSerializer

class Price_typeViewSet(viewsets.ModelViewSet):
    queryset = Price_type.objects.all()
    serializer_class = Price_typeSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(name=name)
        return queryset

class Access_typeViewSet(viewsets.ModelViewSet):
    queryset = Access_type.objects.all()
    serializer_class = Access_typeSerializer
    
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(name=name)
        return queryset

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(name=name)
        return queryset

class AdresseViewSet(viewsets.ModelViewSet):
    queryset = Adresse.objects.all()
    serializer_class = AdresseSerializer
    
    filter_backends = [filters.SearchFilter]
    search_fields = ['address_name']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        address_name = self.request.query_params.get('address_name')
        if address_name is not None:
            queryset = queryset.filter(address_name=address_name)
        return queryset

class AudienceViewSet(viewsets.ModelViewSet):
    queryset = Audience.objects.all()
    serializer_class = AudienceSerializer
    
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(name=name)
        return queryset

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(name=name)
        return queryset
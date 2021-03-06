from quickstart.models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer
from rest_framework.response import Response

# Lead Viewset
class LeadViewSet(viewsets.ModelViewSet): 
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = LeadSerializer

    def get_queryset(self):
        return self.request.user.leads.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


    def get_paginated_response(self, data):
       return Response(data)
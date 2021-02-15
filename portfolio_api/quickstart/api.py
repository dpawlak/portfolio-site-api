from quickstart.models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer
from rest_framework.response import Response

# Lead Viewset
class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer

    def get_paginated_response(self, data):
       return Response(data)
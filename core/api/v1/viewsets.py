from rest_framework import authentication
from core.models import Datesheet
from .serializers import DatesheetSerializer
from rest_framework import viewsets

class DatesheetViewSet(viewsets.ModelViewSet):
    serializer_class = DatesheetSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Datesheet.objects.all()
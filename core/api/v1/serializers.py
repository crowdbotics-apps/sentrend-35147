from rest_framework import serializers
from core.models import Datesheet

class DatesheetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Datesheet
        fields = "__all__"
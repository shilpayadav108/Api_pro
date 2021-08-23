from api.models import Shopper
from rest_framework import serializers
# remember to import the File model
class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()
class SaveFileSerializer(serializers.Serializer):
    
    class Meta:
        model = Shopper
        fields = "__all__"
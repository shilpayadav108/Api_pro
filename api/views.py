from django.shortcuts import render

# Create your views here.
from rest_framework import generics
import pandas
import io, csv, pandas as pd
from rest_framework.response import Response
from .models import Shopper
from .serializers import FileUploadSerializer
from rest_framework import status
import time; 
# remember to import the File model
# remember to import the FileUploadSerializer and SaveFileSerializer
class UploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        
        # df = pd.read_excel("Downloads\\extract\\shopper_actions.csv")
        ticks = time.time()

        reader = pd.read_csv(file)
        
        # file=reader.dropna()
        file=reader.dropna(subset=["publisher_id"])  
        # print(type(file))
        # print(reader)
        # ticks1 = time.time()
        # print(ticks1-ticks)
        
        for index, row in reader.iterrows():
            shopper_file = Shopper(
                
                       action = row["action"],
                       time_stamp = row['time_stamp'],
                       
                       publisher_id= row['publisher_id'],
                      

                       shopper_id= row["shopper_id"],
                       
                       )
            shopper_file.save()
        
        return Response({"status": "success"},
                        status.HTTP_201_CREATED)
                        
            



import csv
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.cache import cache_page

from .models import Diagnosis
from .serializers import DiagnosisSerializer


# Views
@cache_page
class DiagnosisListCreateView(generics.ListCreateAPIView):
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSerializer

@cache_page
class DiagnosisRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSerializer
    
class UploadCSVView(APIView):
    def post(self, request):
        if 'csv_file' not in request.FILES:
            return Response({"error": "No file found"}, status=400)
        
        csv_file = request.FILES['csv_file']
        decoded_file = csv_file.read().decode('utf-8')
        csv_data = csv.reader(decoded_file.splitlines(), delimiter=',')
        next(csv_data)
        
        serializer = DiagnosisSerializer(data=csv_data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"successs": "ICD codes uploaded successfully."})
        else:
            return Response(serializer.errors, status=400)

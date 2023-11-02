from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Survey, Prediction
from .serializers import SurveySerializer, PredictionSerializer

@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello, World!"})

@api_view(['POST'])
def post_survey(request):
    serializer = SurveySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def post_predict(request):
    serializer = PredictionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
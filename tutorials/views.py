from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from tutorials.models import User
from tutorials.serializers import TutorialSerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()

        user_serializer = TutorialSerializer(users, many=True)

        return JsonResponse(user_serializer.data, safe=False)
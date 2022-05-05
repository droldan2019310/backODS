from dataclasses import fields
from rest_framework import serializers 
from tutorials.models import  statusUser, typeUser, User


class TutorialSerializer(serializers.ModelSerializer):


    class Meta:
        model = typeUser
        fields = ('id','description') 

    class Meta:
        model = statusUser
        fields = ('id', 'description')
    
    class Meta:
        model = User
        fields = ('id', 'name','username','email','phone','password','type','status')
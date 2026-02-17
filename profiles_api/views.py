from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import   filters
from profiles_api import permissions
from profiles_api import serializer 
from django.shortcuts import get_object_or_404
from profiles_api import models
class HelloApiView(APIView):
    """TEST API View"""
    serializer_class=serializer.HelloSerializer
    def get(self, request,format=None):
        """Returns a list of ApiView features"""
        an_apiview=[
            'Uses Http method as functoin (get,post,patch,put,delete)'  ,
            'is similar to a traditional Django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
            
        ]
        return Response({'message':"Hello !",'Data':an_apiview})
    
    def post(self,request):
        """Create a hello message with our name """
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({"message":message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk=None):
        """Handle updating an object """    
        return Response({'method':'PUT'})
    
    def patch(self,request,pk=None):
       """Handle  a partial update of an object """    
       return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """Delete an object"""  
        return Response({'method':'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class=serializer.HelloSerializer
    small_list_to_save_data={}
    copy_data={}
    def list(self,request):
        my_infor=[
             'Uses Http method as functoin (get,post,patch,put,delete)'  ,
            'is similar to a traditional Django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return  Response({"message":'Hello! Ebro.',"data":my_infor})

    def create(self,request):
        """Create a new hello message"""
        serializer=self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            email=serializer.validated_data.get('email')
            age=serializer.validated_data.get('age')
            message =f"Hello {name}! Your age is {age}\
                         your email {email}"
            self.small_list_to_save_data[name]={"age":age,"email":email}
            data=self.small_list_to_save_data.copy()
            return Response({"message":message,"data":data})
        
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        
    def retrieve(self,request,pk=None):
        """Handle getting an object by its ID"""    
        self.copy_data=self.small_list_to_save_data.copy()
        data=self.copy_data
        return Response({ "s":"hellofrom retrieve","data":data})
        

    def update(self,request,pk=None):
        """Handle updating an object"""    

        return Response({'http_method':'PUT '})


    def partial_update(self,request,pk=None):
        """Handle update part object"""    
        return Response({'http_method':'Patch '})


    def destroy(self,request,pk=None):
        "Handel REMOVING an object  "
        return Response({'http_method':'DELETE '})

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset=models.UserProfile.objects.all()
    serializer_class=serializer.UserProfileSerializer
    authentication_classes=(TokenAuthentication, )
    permission_classes=(permissions.UpdateOwnProfile,)

    filter_backends=(filters.SearchFilter,)
    search_fields=('name','email')

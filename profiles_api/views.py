from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """TEST API View"""
    def get(self, request,format=None):
        """Returns a list of ApiView features"""
        an_apiview=[
            'Uses Http method as functoin (get,post,patch,put,delete)'  ,
            'is similar to a traditional Django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
            
        ]
        return Response({'message':"Hello !",'Data':an_apiview})
    
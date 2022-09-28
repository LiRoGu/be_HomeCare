from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
#from rest_framework_simplejwt.backends import TokenBackend
#from rest_framework.permissions import IsAuthenticated
from authAppHomeCare.serializers.usuarioSerializer import UsuarioSerializer
from authAppHomeCare.models.usuario import Usuario


class UsuarioListView(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    #permission_classes = (IsAuthenticated,) #ACTIVAR

    def list(self, request):
        print("GET a todos los Usuario")
        queryset = self.get_queryset()
        serializer = UsuarioSerializer(queryset, many=True)
        return Response(serializer.data)

    #def post(self, request, *args, **kwargs):
        #print("POST a Usuario")
        #print(request.data)
        #usuarioData = request.data.pop('usuario')
        #serializerU.is_valid(raise_exception=True)
        #usuario = serializerU.save()
        #return Response(status=status.HTTP_201_CREATED)


class UsuarioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    lookup_field = "id"
    lookup_url_kwarg = 'pk'
    #permission_classes = (IsAuthenticated,)#ACTIVAR

    def get(self, request, *args, **kwargs):
        print("GET a Usuario")
        """if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)"""    
        return super().get(request, *args, **kwargs)

    def put (self, request, *args, **kwargs):
        print("PUT a Usuario")
        """if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)"""    
        return super().put(request, *args, **kwargs)    
            
    def delete (self, request, *args, **kwargs):
        print("DELETE a Usuario")
        """if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)"""    
        return super().delete(request, *args, **kwargs)
    
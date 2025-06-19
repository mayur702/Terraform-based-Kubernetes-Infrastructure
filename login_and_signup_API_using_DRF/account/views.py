from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import generics
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework import status
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

# Create your views here.
class SignupView(generics.ListCreateAPIView):
    permission_classes  = [HasAPIKey]
    serializer_class    = SignupSerializer
    queryset            = User.objects.all().order_by('-id')

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class SigninView(generics.GenericAPIView):
    permission_classes      = [HasAPIKey]
    serializer_class        = SigninSerializer
    queryset                = User.objects.all().order_by('-id')

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Health check endpoint for liveness/readiness probes
@api_view(['GET'])
@permission_classes([AllowAny])
def health_check(request):
    return JsonResponse({'status': 'ok'})


from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status

from gateway.models import User
from gateway.views.base_proxy_view import BaseProxyView
from ..serializers import CustomTokenObtainPairSerializer
import requests 

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class LinkedUserDoctorAPIView(BaseProxyView):
    def get(self, request, user_id, *args, **kwargs):
        try:
            user = User.objects.get(id=user_id)
            linked_user_id = user.linked_user
            
            doctor_url = f'{settings.USER_SERVICE_BASE_API_URL}/doctors/user/{linked_user_id}/'
            
            doctor_response = requests.get(doctor_url)

            if doctor_response.status_code == 200:
                return Response(doctor_response.json(), status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)
        
        except User.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class LinkedUserPatientAPIView(BaseProxyView):
    def get(self, request, user_id, *args, **kwargs):
        try:
            user = User.objects.get(id=user_id)
            linked_user_id = user.linked_user
            
            patient_url = f'{settings.USER_SERVICE_BASE_API_URL}/pacients/user/{linked_user_id}/'
            
            patient_response = requests.get(patient_url)

            if patient_response.status_code == 200:
                return Response(patient_response.json(), status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Patient not found'}, status=status.HTTP_404_NOT_FOUND)
        
        except User.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
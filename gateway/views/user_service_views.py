from rest_framework.permissions import AllowAny
from django.conf import settings
from .base_proxy_view import BaseProxyView

class RegisterDoctorView(BaseProxyView):
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        url = f'{settings.USER_SERVICE_BASE_API_URL}/doctors/'
        return self.proxy('POST', url, request, *args, **kwargs)

class DoctorsServiceProxy(BaseProxyView):
    def get(self, request, path, *args, **kwargs):
        url = f'{settings.USER_SERVICE_BASE_API_URL}/doctors/{path}'
        return self.proxy('GET', url, request, *args, **kwargs)

    def put(self, request, path, *args, **kwargs):
        url = f'{settings.USER_SERVICE_BASE_API_URL}/doctors/{path}'
        return self.proxy('PUT', url, request, *args, **kwargs)
    
class RegisterPatientView(BaseProxyView):
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        url = f'{settings.USER_SERVICE_BASE_API_URL}/pacients/'
        return self.proxy('POST', url, request, *args, **kwargs)
    
class PatientsServiceProxy(BaseProxyView):
    def get(self, request, path, *args, **kwargs):
        url = f'{settings.USER_SERVICE_BASE_API_URL}/pacients/{path}'
        return self.proxy('GET', url, request, *args, **kwargs)

    def put(self, request, path, *args, **kwargs):
        url = f'{settings.USER_SERVICE_BASE_API_URL}/pacients/{path}'
        return self.proxy('PUT', url, request, *args, **kwargs)
    
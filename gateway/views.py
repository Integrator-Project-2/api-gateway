from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from django.conf import settings
from django.http import HttpResponse

class BaseProxyView(APIView):
    def proxy(self, method, url, request, *args, **kwargs):
        response = requests.request(method, url, json=request.data, headers=request.headers)
        return HttpResponse(response.content, status=response.status_code, content_type=response.headers['Content-Type'])

class RegisterPatientView(BaseProxyView):
    def post(self, request, *args, **kwargs):
        url = f'{settings.USER_SERVICE_BASE_API_URL}/pacients/'
        return self.proxy('POST', url, request, *args, **kwargs)

class RegisterDoctorView(BaseProxyView):
    def post(self, request, *args, **kwargs):
        url = f'{settings.USER_SERVICE_BASE_API_URL}/doctors/'
        return self.proxy('POST', url, request, *args, **kwargs)

class ObtainAuthToken(BaseProxyView):
    def post(self, request, *args, **kwargs):
        url = f'{settings.USER_SERVICE_BASE_API_URL}/token/'
        return self.proxy('POST', url, request, *args, **kwargs)

class RefreshAuthToken(BaseProxyView):
    def post(self, request, *args, **kwargs):
        url = f'{settings.USER_SERVICE_BASE_API_URL}/token/refresh/'
        return self.proxy('POST', url, request, *args, **kwargs)

class AssociateDoctorToPatientView(BaseProxyView):
    def post(self, request, *args, **kwargs):
        url = f'{settings.PATIENTS_MANAGMENT_SERVICE_BASE_API_URL}/associate-doctor-patient/'
        return self.proxy('POST', url, request, *args, **kwargs)

class CreateMedicalPrescriptionView(BaseProxyView):
    def post(self, request, *args, **kwargs):
        url = f'{settings.MEDICAL_PRESCRIPTIONS_SERVICE_BASE_API_URL}/medical-prescriptions/'
        return self.proxy('POST', url, request, *args, **kwargs)

class MedicationServiceProxy(BaseProxyView):
    def get(self, request, path, *args, **kwargs):
        url = f'{settings.MEDICATION_SERVICE_BASE_API_URL}/medications/{path}'
        return self.proxy('GET', url, request, *args, **kwargs)

    def post(self, request, path, *args, **kwargs):
        url = f'{settings.MEDICATION_SERVICE_BASE_API_URL}/medications/{path}'
        return self.proxy('POST', url, request, *args, **kwargs)

    def put(self, request, path, *args, **kwargs):
        url = f'{settings.MEDICATION_SERVICE_BASE_API_URL}/medications/{path}'
        return self.proxy('PUT', url, request, *args, **kwargs)

    def delete(self, request, path, *args, **kwargs):
        url = f'{settings.MEDICATION_SERVICE_BASE_API_URL}/medications/{path}'
        return self.proxy('DELETE', url, request, *args, **kwargs)
    
class MedicationSearchServiceProxy(BaseProxyView):
    def get(self, request, path, *args, **kwargs):
        medication_name = request.GET.get('name', '')
        url = f'{settings.MEDICATION_SERVICE_BASE_API_URL}/medications/search/?name={medication_name}/{path}'
        return self.proxy('GET', url, request, *args, **kwargs)
    
class MedicationReminderDueReminderServiceProxy(BaseProxyView):
    def get(self, request, path, *args, **kwargs):
        patient_id = request.GET.get('patient_id', '')
        url = f'{settings.MEDICATION_SERVICE_BASE_API_URL}/medication-reminder/due_reminders/?patient_id={patient_id}/{path}'
        return self.proxy('GET', url, request, *args, **kwargs)

class DoctorsServiceProxy(BaseProxyView):
    def get(self, request, path, *args, **kwargs):
        url = f'{settings.USER_SERVICE_BASE_API_URL}/doctors/{path}'
        return self.proxy('GET', url, request, *args, **kwargs)

    def post(self, request, path, *args, **kwargs):
        url = f'{settings.USER_SERVICE_BASE_API_URL}/doctors/{path}'
        return self.proxy('POST', url, request, *args, **kwargs)

    def put(self, request, path, *args, **kwargs):
        url = f'{settings.USER_SERVICE_BASE_API_URL}/doctors/{path}'
        return self.proxy('PUT', url, request, *args, **kwargs)

class PatientsServiceProxy(BaseProxyView):
    def get(self, request, path, *args, **kwargs):
        url = f'{settings.USER_SERVICE_BASE_API_URL}/pacients/{path}'
        return self.proxy('GET', url, request, *args, **kwargs)

    def post(self, request, path, *args, **kwargs):
        url = f'{settings.USER_SERVICE_BASE_API_URL}/pacients/{path}'
        return self.proxy('POST', url, request, *args, **kwargs)

    def put(self, request, path, *args, **kwargs):
        url = f'{settings.USER_SERVICE_BASE_API_URL}/pacients/{path}'
        return self.proxy('PUT', url, request, *args, **kwargs)

class MedicationReminderServiceProxy(BaseProxyView):
    def get(self, request, path, *args, **kwargs):
        url = f'{settings.MEDICATION_SERVICE_BASE_API_URL}/{path}'
        return self.proxy('GET', url, request, *args, **kwargs)

    def post(self, request, path, *args, **kwargs):
        url = f'{settings.MEDICATION_SERVICE_BASE_API_URL}/{path}'
        return self.proxy('POST', url, request, *args, **kwargs)

    def put(self, request, path, *args, **kwargs):
        url = f'{settings.MEDICATION_SERVICE_BASE_API_URL}/{path}'
        return self.proxy('PUT', url, request, *args, **kwargs)

    def patch(self, request, path, *args, **kwargs):
        url = f'{settings.MEDICATION_SERVICE_BASE_API_URL}/{path}'
        return self.proxy('PATCH', url, request, *args, **kwargs)

    def delete(self, request, path, *args, **kwargs):
        url = f'{settings.MEDICATION_SERVICE_BASE_API_URL}/{path}'
        return self.proxy('DELETE', url, request, *args, **kwargs)

class AmountReminderServiceProxy(BaseProxyView):
    def get(self, request, path, *args, **kwargs):
        url = f'{settings.MEDICATION_SERVICE_BASE_API_URL}/amount-reminder/{path}'
        return self.proxy('GET', url, request, *args, **kwargs)

    def post(self, request, path, *args, **kwargs):
        url = f'{settings.MEDICATION_SERVICE_BASE_API_URL}/amount-reminder/{path}'
        return self.proxy('POST', url, request, *args, **kwargs)

    def put(self, request, path, *args, **kwargs):
        url = f'{settings.MEDICATION_SERVICE_BASE_API_URL}/amount-reminder/{path}'
        return self.proxy('PUT', url, request, *args, **kwargs)

    def patch(self, request, path, *args, **kwargs):
        url = f'{settings.MEDICATION_SERVICE_BASE_API_URL}/amount-reminder/{path}'
        return self.proxy('PATCH', url, request, *args, **kwargs)

    def delete(self, request, path, *args, **kwargs):
        url = f'{settings.MEDICATION_SERVICE_BASE_API_URL}/amount-reminder/{path}'
        return self.proxy('DELETE', url, request, *args, **kwargs)


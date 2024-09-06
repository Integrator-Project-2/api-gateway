from django.conf import settings
from .base_proxy_view import BaseProxyView


class AssociateDoctorToPatientView(BaseProxyView):
    def post(self, request, *args, **kwargs):
        url = f'{settings.PATIENTS_MANAGMENT_SERVICE_BASE_API_URL}/associate-doctor-patient/'
        return self.proxy('POST', url, request, *args, **kwargs)
    
class DoctorPatientsListView(BaseProxyView):
    def get(self, request, doctor_id, *args, **kwargs):
        url = f'{settings.PATIENTS_MANAGMENT_SERVICE_BASE_API_URL}/doctors/{doctor_id}/patients/'
        return self.proxy('GET', url, request, *args, **kwargs)
    
class CreateMedicalPrescriptionView(BaseProxyView):
    def post(self, request, *args, **kwargs):
        url = f'{settings.PATIENTS_MANAGMENT_SERVICE_BASE_API_URL}/medical-prescriptions/'
        return self.proxy('POST', url, request, *args, **kwargs)

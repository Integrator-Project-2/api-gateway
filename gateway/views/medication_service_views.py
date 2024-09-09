from django.conf import settings
from .base_proxy_view import BaseProxyView
    
class MedicationServiceProxy(BaseProxyView):
    def get(self, request, path, *args, **kwargs):
        medication_name = request.GET.get('name', '')

        if medication_name:
            url = f'{settings.MEDICATION_SERVICE_BASE_API_URL}/medications/{path}?name={medication_name}'
        else:
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
    
# class MedicationSearchServiceProxy(BaseProxyView):
#     def get(self, request, path, *args, **kwargs):
#         medication_name = request.GET.get('name', '')
#         url = f'{settings.MEDICATION_SERVICE_BASE_API_URL}/medications/{path}'
#         return self.proxy('GET', url, request, *args, **kwargs)
    
class MedicationReminderRecordsServiceProxy(BaseProxyView):
    def get(self, request, path, *args, **kwargs):
        patient_id = request.GET.get('patient_id', '')
        reminder_id = request.GET.get('reminder_id', '')
        
        if patient_id:
            url = f'{settings.MEDICATION_SERVICE_BASE_API_URL}/medication-reminder-record/{path}?patient_id={patient_id}'

        elif reminder_id:
            url = f'{settings.MEDICATION_SERVICE_BASE_API_URL}/medication-reminder-record/{path}?reminder_id={reminder_id}'

        else:
            url = f'{settings.MEDICATION_SERVICE_BASE_API_URL}/medication-reminder-record/{path}'
        
        return self.proxy('GET', url, request, *args, **kwargs)
    
class TakeMedicationServiceProxy(BaseProxyView):
    def post(self, request, reminder_record_id, *args, **kwargs):
        url = f'{settings.MEDICATION_SERVICE_BASE_API_URL}/medication-reminder-record/{reminder_record_id}/take-medication/'
        return self.proxy('POST', url, request, *args, **kwargs)
class UpcomingReminderRecordServiceProxy(BaseProxyView):
    def get(self, request, *args, **kwargs):
        patient_id = request.GET.get('patient_id', '')
        url = f'{settings.MEDICATION_SERVICE_BASE_API_URL}/medication-reminder-record/upcoming/?patient_id={patient_id}'

        return self.proxy('GET', url, request, *args, **kwargs)

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
    
class MedicationReminderServiceProxy(BaseProxyView):
    def get(self, request, path, *args, **kwargs):
        patient_id = request.GET.get('patient_id', '')
        if patient_id:
            url = f'{settings.MEDICATION_SERVICE_BASE_API_URL}/medication-reminder/{path}?patient_id={patient_id}'
        else:
            url = f'{settings.MEDICATION_SERVICE_BASE_API_URL}/medication-reminder/{path}'

        return self.proxy('GET', url, request, *args, **kwargs)

    def post(self, request, path, *args, **kwargs):
        url = f'{settings.MEDICATION_SERVICE_BASE_API_URL}/medication-reminder/{path}'
        return self.proxy('POST', url, request, *args, **kwargs)

    def delete(self, request, path, *args, **kwargs):
        url = f'{settings.MEDICATION_SERVICE_BASE_API_URL}/medication-reminder/{path}'
        return self.proxy('DELETE', url, request, *args, **kwargs)
    
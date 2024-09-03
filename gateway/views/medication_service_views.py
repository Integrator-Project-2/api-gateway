from django.conf import settings
from .base_proxy_view import BaseProxyView
    
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
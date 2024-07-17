from django.urls import path, re_path
from .views import (
    MedicationReminderDueReminderServiceProxy, MedicationSearchServiceProxy, RegisterPatientView, RegisterDoctorView, ObtainAuthToken, 
    RefreshAuthToken, AssociateDoctorToPatientView, 
    CreateMedicalPrescriptionView, MedicationServiceProxy,
    DoctorsServiceProxy, PatientsServiceProxy, MedicationReminderServiceProxy,
    AmountReminderServiceProxy
)

urlpatterns = [
    path('register-patient/', RegisterPatientView.as_view(), name='register-patient'),
    path('register-doctor/', RegisterDoctorView.as_view(), name='register-doctor'),
    path('auth-token/', ObtainAuthToken.as_view(), name='auth-token'),
    path('auth-token/refresh/', RefreshAuthToken.as_view(), name='auth-token-refresh'),
    path('associate-doctor-patient/', AssociateDoctorToPatientView.as_view(), name='associate-doctor-patient'),
    path('create-medical-prescription/', CreateMedicalPrescriptionView.as_view(), name='create-medical-prescription'),
    re_path(r'^medications/(?P<path>.*)$', MedicationServiceProxy.as_view(), name='medication-service'),
    re_path(r'^medications/search$', MedicationSearchServiceProxy.as_view(), name='medication-search-service'),
    re_path(r'^medications/due-reminders$', MedicationSearchServiceProxy.as_view(), name='medication-search-service'),
    re_path(r'^doctors-service/(?P<path>.*)$', DoctorsServiceProxy.as_view(), name='doctors-service'),
    re_path(r'^patients-service/(?P<path>.*)$', PatientsServiceProxy.as_view(), name='patients-service'),
    re_path(r'^medication-reminder/(?P<path>.*)$', MedicationReminderDueReminderServiceProxy.as_view(), name='medication-reminder-service'),
    re_path(r'^amount-reminder/(?P<path>.*)$', AmountReminderServiceProxy.as_view(), name='amount-reminder-service'),
]

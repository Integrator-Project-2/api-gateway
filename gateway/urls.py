from django.urls import path, re_path

from gateway.views.create_user_view import CreateUserView
from gateway.views.medication_service_views import AmountReminderServiceProxy, MedicationReminderDueReminderServiceProxy, MedicationSearchServiceProxy, MedicationServiceProxy
from gateway.views.patient_managment_views import AssociateDoctorToPatientView, CreateMedicalPrescriptionView, DoctorPatientsListView, PatientMedicationsAPIView, PatientPrescriptionsAPIView
from gateway.views.user_service_views import DoctorsServiceProxy, PatientsServiceProxy, RegisterDoctorView, RegisterPatientView, SearchPatientByCPFView


urlpatterns = [
    path('create-user/', CreateUserView.as_view(), name='create-user'),
    path('register-patient/', RegisterPatientView.as_view(), name='register-patient'),
    path('register-doctor/', RegisterDoctorView.as_view(), name='register-doctor'),
    path('associate-doctor-patient/', AssociateDoctorToPatientView.as_view(), name='associate-doctor-patient'),
    path('create-medical-prescription/', CreateMedicalPrescriptionView.as_view(), name='create-medical-prescription'),
    re_path(r'^medications/(?P<path>.*)$', MedicationServiceProxy.as_view(), name='medication-service'),
    re_path(r'^medications/search$', MedicationSearchServiceProxy.as_view(), name='medication-search-service'),
    re_path(r'^medications/due-reminders$', MedicationSearchServiceProxy.as_view(), name='medication-search-service'),
    re_path(r'^doctors-service/(?P<path>.*)$', DoctorsServiceProxy.as_view(), name='doctors-service'),
    re_path(r'^patients-service/(?P<path>.*)$', PatientsServiceProxy.as_view(), name='patients-service'),
    re_path(r'^medication-reminder/(?P<path>.*)$', MedicationReminderDueReminderServiceProxy.as_view(), name='medication-reminder-service'),
    re_path(r'^amount-reminder/(?P<path>.*)$', AmountReminderServiceProxy.as_view(), name='amount-reminder-service'),
    re_path(r'^pacients-service/search-by-cpf/(?P<path>.*)?$', SearchPatientByCPFView.as_view(), name='search-patient-by-cpf'),
    path('doctors/<int:doctor_id>/patients/', DoctorPatientsListView.as_view(), name='doctor-patients-list'),
    re_path(r'^prescriptions/patient/(?P<patient_id>\d+)/$', PatientPrescriptionsAPIView.as_view(), name='doctor-patients-list'),
     re_path(r'^medications-patient/(?P<patient_id>\d+)/$', PatientMedicationsAPIView.as_view(), name='patient-medications'),
]

from django.urls import path
from .views import RegisterView, ProfileView, PatientDashboardView ,CaregiverDashboardView ,AdminDashboardView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('patient-dashboard/', PatientDashboardView.as_view(), name='patient-dashboard'),
    path('caregiver-dashboard/',CaregiverDashboardView.as_view(),name='caregiver-dashboard'),
    path('admin-dashboard/',AdminDashboardView.as_view(),name='admin-dashboard'),
]
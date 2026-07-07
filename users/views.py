from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsPatient
from .permissions import IsPatient, IsCaregiver, IsAdmin
from .models import User
from .serializers import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        data = {
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "phone_number": user.phone_number,
            "role": user.role,
        }

        return Response(data)
class PatientDashboardView(APIView):
    permission_classes = [IsPatient]

    def get(self, request):
        return Response({
            "message": "Welcome to the Patient Dashboard",
            "user": request.user.username,
            "role": request.user.role
        })
class CaregiverDashboardView(APIView):
    permission_classes = [IsCaregiver]

    def get(self, request):
        return Response({
            "message": "Welcome to the Caregiver Dashboard",
            "user": request.user.username,
            "role": request.user.role
        })
class AdminDashboardView(APIView):
    permission_classes = [IsAdmin]

    def get(self, request):
        return Response({
            "message": "Welcome to the Admin Dashboard",
            "user": request.user.username,
            "role": request.user.role
        })
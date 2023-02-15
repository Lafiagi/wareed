# Django Imports
from django.contrib.auth import logout
from django.db import transaction
from django.conf import settings

# Rest Framework Imports
from rest_framework import generics, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated

# Third Party Imports
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Own Imports
from authy.models import User, Student
from authy.filters import StudentFilter
from authy.serializers import (
    UserLoginObtainPairSerializer,
    UserTokenRefreshSerializer,
    UserSerializer,
    StudentSerializer,
)
from authy.tasks import send_welcome_mail


class LoginUserAPIView(TokenObtainPairView):
    """Responsible for authenticatiing user."""

    serializer_class = UserLoginObtainPairSerializer


class RefreshLoginUserAPIView(TokenRefreshView):
    """Responsible for refreshing user access token."""

    serializer_class = UserTokenRefreshSerializer


class LogoutAPIView(generics.GenericAPIView):
    """Responsible for logging out the authenticated user."""
    serializer_class = UserSerializer
    
    def post(self, request: Request) -> Response:
        logout(request)
        payload = {
            "status": status.HTTP_200_OK,
            "message": "Logged out successful!",
        }
        return Response(data=payload, status=status.HTTP_200_OK)


class UsersViewset(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [AllowAny,]
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = [
        "full_name",
    ]

    @transaction.atomic
    def create(self, request, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        send_welcome_mail.delay(
            name=serializer.validated_data.get("full_name"),
            user_email=serializer.validated_data.get("email"),
        )
        response_payload = {
            "status": status.HTTP_201_CREATED,
            "message": "Successfully created user",
            "success": True,
            "data": serializer.data,
        }

        return Response(response_payload, status=status.HTTP_201_CREATED)


class StudentViewset(ModelViewSet):
    queryset = Student.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend,]
    filterset_class = StudentFilter


class SendMailView(generics.GenericAPIView):
    """Responsible for sending mail to a user."""
    permission_classes = [IsAuthenticated]
    
    def post(self, request: Request, student_id: int) -> Response:
        try:
            student = Student.objects.get(id=int(student_id))
            email = student.student_email
            name = student.student_name    
            send_welcome_mail(name, email)
        
        except Student.DoesNotExist:    
            payload = {
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Invalid student id!",
            }
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
        
        payload = {
                "status": status.HTTP_200_OK,
                "message": "Mail sent successfuly!",
            }
        return Response(data=payload, status=status.HTTP_200_OK)
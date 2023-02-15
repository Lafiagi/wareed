# Django Imports
from django.urls import path

# rest framework imports
from rest_framework import routers
from authy.models import User

# Own Imports
from authy.views import (
    UsersViewset,
    LoginUserAPIView,
    RefreshLoginUserAPIView,
    LogoutAPIView,
    StudentViewset,
    SendMailView
)


router = routers.SimpleRouter()
router.register(r"user", UsersViewset, basename="create_user")
router.register(r"student", StudentViewset, basename="create_student")

app_name = "authy"

urlpatterns = [
    path("login/", LoginUserAPIView.as_view(), name="login"),
    path(
        "login/refresh/",
        RefreshLoginUserAPIView.as_view(),
        name="login_refresh",
    ),
    path("logout/", LogoutAPIView.as_view(), name="logout"),
    path(
        "<int:student_id>/mail/",
        SendMailView.as_view(),
        name="send_mail",
    ),
]
urlpatterns += router.urls

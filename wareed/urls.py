# Django Imports
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt

# Third Party Imports
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Rest Framework Imports
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

# Schema Definition
schema_view = get_schema_view(
    openapi.Info(
        title="Wareed",
        default_version="v1",
        description="",
        contact=openapi.Contact(email="admin@wareed.sa"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


@csrf_exempt
@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def home(request):
    """Handle default request."""
    return Response(data="This is the Wareed Assessment API")


urlpatterns = [
    path(":xyz:/bilal/", admin.site.urls),
    path("", home),
    path("api/auth/", include("authy.urls")),
]

if settings.DEBUG:
    urlpatterns += [
        # Swagger docs
        re_path(
            r"^generate_api_docs(?P<format>\.json|\.yaml)$",
            schema_view.without_ui(cache_timeout=0),
            name="schema-json",
        ),
        re_path(
            r"^docs/$",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="api_docs",
        ),
    ]
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )


admin.site.site_header = "Wareed Admin"
admin.site.index_title = "Home page"
admin.site.site_title = "Entities page"

from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from django.contrib import admin
from django.urls import include, path, re_path

schema_view = get_schema_view(
    openapi.Info(
        title="YS Python Challenge API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://blabla.terms.com",
        contact=openapi.Contact(email="test@dev.com"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.IsAuthenticated,),
)

urlpatterns = [
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    re_path(r"^swagger/$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    re_path(r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path(
        "admin/",
        admin.site.urls,
    ),
    path(
        "api/v1/orders/",
        include("orders.api.v1.urls"),
    ),
]

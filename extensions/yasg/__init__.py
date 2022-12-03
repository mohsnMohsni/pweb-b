# Core imports.
from django.urls import path

# Third-party imports.
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from drf_yasg.generators import OpenAPISchemaGenerator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication


def lazy_schema_generator(app_name: str):
    class SchemaGenerator(OpenAPISchemaGenerator):
        def coerce_path(self, path, view):
            _ = super().coerce_path(path, view)
            return f'/{app_name}{_}'

        def determine_path_prefix(self, paths):
            return ''

    return SchemaGenerator


LOCAL_APPS = {
    'accounts',
}


schema_view = get_schema_view(
    openapi.Info(
        title="Core API docs",
        default_version='v1',
    ),
    public=True,
    authentication_classes=[
        SessionAuthentication,
    ],
    permission_classes=[
        IsAuthenticated,
    ],
)


apps_urlpatterns: list = list()


for app in LOCAL_APPS:
    app_schema_view = get_schema_view(
        openapi.Info(
            title="Core API docs",
            default_version='v1',
            description="swagger docs",
        ),
        public=True,
        authentication_classes=[
            SessionAuthentication,
        ],
        permission_classes=[
            IsAuthenticated,
        ],
        generator_class=lazy_schema_generator(app),
        urlconf=f'apps.{app}.urls',
    )
    apps_urlpatterns.extend(
        [
            path(f'swagger/{app}/', app_schema_view.with_ui('swagger', cache_timeout=0)),
            path(f'redoc/{app}/', app_schema_view.with_ui('redoc', cache_timeout=0)),
        ]
    )


class SwaggerIndexAPIView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]
    authentication_classes = [
        SessionAuthentication,
    ]

    def get(self, request) -> Response:
        base_path: str = '{}://{}'.format(request.scheme, request.get_host())
        return Response({app: f'{base_path}/swagger/{app}/' for app in LOCAL_APPS})


class RedocIndexAPIView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]
    authentication_classes = [
        SessionAuthentication,
    ]

    def get(self, request) -> Response:
        base_path: str = '{}://{}'.format(request.scheme, request.get_host())
        return Response({app: f'{base_path}/redoc/{app}/' for app in LOCAL_APPS})


urlpatterns = [
    path('swagger/', SwaggerIndexAPIView.as_view(), name='swagger-index-page'),
    path('redoc/', RedocIndexAPIView.as_view(), name='redoc-index-page'),
    path('swagger/all/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/all/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + apps_urlpatterns

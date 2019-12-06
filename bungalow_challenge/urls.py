'''
Adding routes for "admin", rest endoints, and Swagger docs
'''

from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers, permissions
from bungalow import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Bungalow Challenge API",
        default_version='v1',
        description="Bugalow!",
        contact=openapi.Contact(email="danielraymie@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,) # no auth
)

router = routers.DefaultRouter()
router.register(r'Property', views.PropertyViewSet)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc',cache_timeout=0), name='schema-redoc'),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

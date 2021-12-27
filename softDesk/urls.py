from django.urls import path, include
from django.contrib import admin
from rest_framework import routers

from app import views

router = routers.SimpleRouter()
router.register('project', views.ProjectViewset, basename='project')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]

from django.urls import path, include
from django.contrib import admin

from app import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/sign-up/', views.SignUp.as_view(), name='sign-up'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/project/', views.Project_list.as_view()),
    path('api/project/<int:pk>/', views.Project_detail.as_view()),
    path('api/project/<int:project_id>/users/', views.ContributorProject.as_view()),
]

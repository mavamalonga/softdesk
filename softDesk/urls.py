from django.urls import path, include
from django.contrib import admin

from app import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/sign-up/', views.SignUpView.as_view(), name='sign-up'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/project/', views.ProjectView.as_view()),
    path('api/project/<int:project_id>/', views.ProjectViewDetail.as_view()),
    path('api/project/<int:project_id>/users/', views.ContributorView.as_view()),
    path('api/project/<int:project_id>/users/<int:user>/', views.ContributorViewDetail.as_view()),
    path('api/project/<int:project_id>/issues/', views.IssueView.as_view()),
    path('api/project/<int:project_id>/issues/<int:issue_id>/', views.IssueDetail.as_view()),
    path('api/project/<int:project_id>/issues/<int:issue_id>/comments/', views.Comment.as_view()),
    path('api/project/<int:project_id>/issues/<int:issue_id>/comments/<int:comment_id>', views.CommentDetail.as_view())
]

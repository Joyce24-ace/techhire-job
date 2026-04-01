# content/urls.py
from django.urls import path
from .views import JobPostingListAPIView, JobPostingDetailAPIView, DemoDashboardView

urlpatterns = [
    path('', DemoDashboardView.as_view(), name='demo-dashboard'),
    path('jobs/', JobPostingListAPIView.as_view(), name='job-list'),
    path('jobs/<int:pk>/', JobPostingDetailAPIView.as_view(), name='job-detail'),
]
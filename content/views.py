from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from .models import JobPosting
from .serializers import JobPostingSerializer
from django.views.generic import TemplateView


class DemoDashboardView(TemplateView):
    template_name = 'content/demo.html'


class JobPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'

class JobPostingListAPIView(generics.ListAPIView):
    """
    List view with Search and Filtering.
    Open to all users, but serializer handles data masking.
    """
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer
    pagination_class = JobPagination
    
    # Search & Filtering Engine
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Requirement: Filter by location
    filterset_fields = ['location'] 
    
    # Requirement: Search title and description
    search_fields = ['title', 'description'] 
    
    # Requirement: Order by created_at (newest first)
    ordering = ['-created_at'] 
    ordering_fields = ['created_at']

class JobPostingDetailAPIView(generics.RetrieveAPIView):
    """
    Retrieve a single Job Detail.
    """
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # Connects to the standard Django User
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        status = "Premium" if self.is_premium else "Basic"
        return f"{self.user.username} - {status}"

class JobPosting(models.Model):
    # Core Fields
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=100)
    
    # Sensitive Fields (to be masked for Basic users)
    company_name = models.CharField(max_length=255)
    salary_range = models.CharField(max_length=100)
    application_link = models.URLField()
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Ensures newest jobs always appear first
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} at {self.company_name}"
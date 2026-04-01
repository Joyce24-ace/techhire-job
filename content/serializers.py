
from rest_framework import serializers
from .models import JobPosting

class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        fields = [
            'id', 'title', 'description', 'location', 
            'company_name', 'salary_range', 'application_link', 'created_at'
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        
        # Correctly checks the 'profile' related name and 'is_premium' field
        is_premium_user = (
            request and 
            request.user.is_authenticated and 
            hasattr(request.user, 'profile') and
            request.user.profile.is_premium 
        )

        # Apply Field-Level Masking if they aren't premium
        if not is_premium_user:
            mask_text = "🔒 Premium Feature"
            data['company_name'] = mask_text
            data['salary_range'] = mask_text
            data['application_link'] = mask_text
            
        return data
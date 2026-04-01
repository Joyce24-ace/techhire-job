from django.core.management.base import BaseCommand
from content.models import JobPosting

class Command(BaseCommand):
    help = 'Imports sample job postings into the database'

    def handle(self, *args, **kwargs):
       
        jobs = [
            {
                "title": "Junior Python Developer",
                "description": "Looking for a Python enthusiast to join our backend team.",
                "location": "Remote",
                "company_name": "TechFlow Inc.",
                "salary_range": "$70k - $90k",
                "application_link": "https://example.com/apply/python"
            },
            {
                "title": "Senior Django Engineer",
                "description": "Lead the development of our premium job board scaling project.",
                "location": "New York",
                "company_name": "FinanceNews Portal",
                "salary_range": "$140k - $180k",
                "application_link": "https://example.com/apply/django"
            },
            {
                "title": "Backend Intern",
                "description": "Great opportunity for students to learn Django and REST Framework.",
                "location": "Austin, TX",
                "company_name": "HealthDaily Apps",
                "salary_range": "$25/hour",
                "application_link": "https://example.com/apply/intern"
            }
        ]

        for data in jobs:
            JobPosting.objects.get_or_create(**data)
            
        self.stdout.write(self.style.SUCCESS('Successfully imported sample job postings.'))
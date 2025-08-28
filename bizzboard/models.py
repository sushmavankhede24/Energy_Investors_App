from django.db import models
from network.models import Company
from django.utils import timezone
# Create your models here.

class Opportunity(models.Model):
    TYPE_CHOICES = [
        ("OFFER", "Offer"),
        ("REQUEST", "Request"),
        ("JOB", "Job"),
    ]
    
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    title = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name = "opportunities", null= True, blank=True)
    location = models.CharField(max_length=120, blank=True)
    description = models.TextField(null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField(default=timezone.now, null = True, blank = True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ["-created_at"]
        
    def __str__(self):
        return f"{self.get_type_display()}: {self.title}"
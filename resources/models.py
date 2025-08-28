from django.db import models

# Create your models here.
class Resource(models.Model):
    TYPE_CHOICES = [
        ("ARTICLE", "Article"),
        ("REPORT", "Report"),
        ("WEBINAR", "Webinar"),
        ("VIDEO", "Video"),
        ("INFOGRAPHIC", "Infographic"),
    ]
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    title = models.CharField(max_length=200)
    summary = models.TextField(blank=True)
    link = models.URLField(blank=True)
    published_at = models.DateField(null=True)
    
    class Meta:
        ordering = ["-published_at", "title"]
        
    def __str__(self):
        return self.title
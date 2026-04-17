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

    def get_embed_url(self):
        if not self.link:
            return ""
    
        if "watch?v=" in self.link:
            video_id = self.link.split("watch?v=")[-1].split("&")[0]
            return f"https://www.youtube.com/embed/{video_id}"
    
        if "youtu.be/" in self.link:
            video_id = self.link.split("youtu.be/")[-1]
            return f"https://www.youtube.com/embed/{video_id}"
    
        return self.link
    
    class Meta:
        ordering = ["-published_at", "title"]
        
    def __str__(self):
        return self.title
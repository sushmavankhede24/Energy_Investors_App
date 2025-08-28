from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=150, blank=True)
    description = models.TextField(blank=True)
    registration_url = models.URLField(blank=True)

    class Meta:
        ordering = ["start_date"]

    def __str__(self):
        return self.title

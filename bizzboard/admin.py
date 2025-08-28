from django.contrib import admin
from .models import Opportunity
# Register your models here.
@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'company', 'is_active', 'created_at', 'expired_at')
    list_filter = ('type', 'is_active', 'company')
    search_fields = ('title', 'description')
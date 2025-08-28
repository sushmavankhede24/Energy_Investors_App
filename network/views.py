from django.shortcuts import render
from .models import Company
# Create your views here.

def company_list(request):
    companies = Company.objects.all().order_by("name")
    return render(request, "network/company_list.html", {"companies": companies})
# views.py
from django.shortcuts import render
from .models import Opportunity
from django.utils import timezone
from django.core.serializers import serialize
import json

# def opportunity_list(request):
#     # Pass all active and non-expired opportunities
#     opportunities = Opportunity.objects.filter(is_active=True, expired_at__gte=timezone.now())

#     # Get the initial search query, if any
#     q = request.GET.get("q", "")

#     # Serialize the queryset to a JSON string
#     opportunities_json = json.loads(serialize("json", opportunities, use_natural_foreign_keys=True))

#     return render(request, "bizzboard/opportunity_list.html", {
#         "opportunities": opportunities_json,
#         "q": q
#     })

def opportunity_list(request):
    opportunities = Opportunity.objects.all()  # Temporarily remove filters
    q = request.GET.get("q", "")
    opportunities_json = json.loads(serialize("json", opportunities, use_natural_foreign_keys=True))
    return render(request, "bizzboard/opportunity_list.html", {
        "opportunities": opportunities_json,
        "q": q
    })
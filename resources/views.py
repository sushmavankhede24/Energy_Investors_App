from django.shortcuts import render
from django_filters import rest_framework as filters
from .models import Resource
# Create your views here.


def resource_list(request):
    qtype = request.GET.get("type", "")
    qs = Resource.objects.all()
    if qtype:
        qs = qs.filter(type=qtype)
    types = dict(Resource.TYPE_CHOICES)
    return render(request, "resources/resource_list.html", {"resources": qs, "types": types, "qtype": qtype})

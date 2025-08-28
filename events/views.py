from django.shortcuts import render
from .models import Event
# Create your views here.

def event_list(request):
    return render(request, "events/event_list.html", {"events": Event.objects.all()})
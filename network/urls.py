from django.urls import path
from . import views
urlpatterns = [
    path("", views.company_list, name="company_list"),
]

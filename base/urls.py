from django.views.generic import TemplateView
from django.urls import path

app_name = "base"

urlpatterns = [
    path("", TemplateView.as_view(template_name="base/index.html")),
]

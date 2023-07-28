from django.urls import path

from .views import ShowList, ShowDetail

app_name = "api"

urlpatterns = [
    path("show/<int:pk>/", ShowDetail.as_view(), name="detailcreate"),
    path("show/", ShowList.as_view(), name="listcreate"),
]

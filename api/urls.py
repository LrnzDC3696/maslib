from django.urls import path

from .views import IndexView, ShowList, ShowDetail

app_name = "api"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("shows/<int:pk>/", ShowDetail.as_view(), name="show-detailcreate"),
    path("shows/", ShowList.as_view(), name="show-listcreate"),
    # /shows/ - GET, POST (by admin),
    # /shows/<int:pk> - GET, PUT + PATCH + DELETE (by admin),
    # /users/ - GET, POST (by admin only),
    # /users/<int:pk>/ - GET, PUT + PATCH + DELETE (by admin or user),
    # /users/<int:pk>"/show-list/ - GET (all non-private), POST + PATCH + DELETE (by admin or user)
    # /users/<int:pk>"/show-list/<int:pk>/ - GET (if non private), POST + PATCH + DELETE (by admin or user)
]

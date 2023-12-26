from django.urls import include, path
from rest_framework import routers
from . import views
from .api.v1.views import itemDetail

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
# router.register(r"items", views.ItemViewSet)
router.register(r"items", views.ItemViewSet, basename="item")
router.register(r"upload", views.UploadViewSet, basename="upload")
router.register(r"api/v1/test/", itemDetail, basename="upload")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

app_name = "inventory"
urlpatterns = [
    path("", include(router.urls)),
    path("api/v1/", include("inventory.api.v1.urls")),
    path("add_item/", views.add_item, name="add_item"),
    path(
        "api-auth/",
        include("rest_framework.urls", namespace="rest_framework"),
    ),
]

from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r"items", views.ItemViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

app_name = "inventory"
urlpatterns = [
    path("", include(router.urls)),
    path("add_item", views.add_item, name="add_item"),
    path(
        "api-auth/",
        include("rest_framework.urls", namespace="rest_framework"),
    ),
]

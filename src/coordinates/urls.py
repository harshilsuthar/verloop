from . import views
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("getAddressDetails", views.getAddressDetails, basename="getAddressDetails")
urlpatterns = router.urls

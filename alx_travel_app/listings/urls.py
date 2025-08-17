from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ListingViewSet, BookingViewSet, InitiatePaymentView, VerifyPaymentView


router = DefaultRouter()
router.register(r'listing', ListingViewSet)
router.register(r'booking', BookingViewSet)
# router.register(r'initiate-payment', InitiatePaymentView, basename='initiate-payment')
# router.register(r'verify-payment', VerifyPaymentView, basename='verify-payment')


urlpatterns = [
    path('', include(router.urls)),
    path("initiate-payment/", InitiatePaymentView.as_view(), name="initiate-payment"),
    path("verify-payment/", VerifyPaymentView.as_view(), name="verify-payment"),
]
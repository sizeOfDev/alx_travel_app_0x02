from django.shortcuts import render
from .serializers import ListingSerializer, BookingSerializer
from .models import Listing, Booking,Payment
import requests
from rest_framework.viewsets import ModelViewSet
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status



class ListingViewSet(ModelViewSet):
    serializer_class = ListingSerializer
    queryset = Listing.objects.all()


class BookingViewSet(ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()


class InitiatePaymentView(APIView):
    def post(self, request):
        booking_reference = request.data.get("booking_reference")
        amount = request.data.get("amount")
        email = request.data.get("email")

        headers = {
            "Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}",
            "Content-Type": "application/json",
        }

        payload = {
            "amount": amount,
            "currency": "ETB",
            "email": email,
            "tx_ref": booking_reference,  # unique per transaction
            "callback_url": "http://localhost:8000/api/verify-payment/",
            "return_url": "http://localhost:8000/payment-success/",
        }

        try:
            response = requests.post(
                f"{settings.CHAPA_BASE_URL}/transaction/initialize",
                json=payload,
                headers=headers,
            )
            data = response.json()

            if data.get("status") == "success":
                transaction_id = data["data"]["tx_ref"]

                Payment.objects.create(
                    booking_reference=booking_reference,
                    transaction_id=transaction_id,
                    amount=amount,
                    status="Pending",
                )

                return Response(data, status=status.HTTP_200_OK)

            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class VerifyPaymentView(APIView):
    def get(self, request):
        tx_ref = request.query_params.get("tx_ref")

        headers = {
            "Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}",
        }

        try:
            response = requests.get(
                f"{settings.CHAPA_BASE_URL}/transaction/verify/{tx_ref}",
                headers=headers,
            )
            data = response.json()

            payment = Payment.objects.filter(transaction_id=tx_ref).first()
            if payment:
                if data.get("status") == "success":
                    payment.status = "Completed"
                else:
                    payment.status = "Failed"
                payment.save()

            return Response(data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

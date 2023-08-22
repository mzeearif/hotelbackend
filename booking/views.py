# from django.shortcuts import render
# from rest_framework import generics
#
# # from rest_framework import generics
# from .models import Reservation, Room, Customer, Booking
# from .serializers import ReservationSerializer, RoomSerializer, CustomerSerializer, BookingSerializer
#
#
# class ReservationListCreateView(generics.ListCreateAPIView):
#     queryset = Reservation.objects.all()
#     serializer_class = ReservationSerializer
#
#
# class RoomListCreateView(generics.ListCreateAPIView):
#     queryset = Room.objects.all()
#     serializer_class = RoomSerializer
#
#
# class CustomerListCreateView(generics.ListCreateAPIView):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer
#
#
# class BookingListCreateView(generics.ListCreateAPIView):
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer
#
# # Create your views here.


from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Room, Price, Unavailable, Limits, Extra, Customer, Booking, Report
from .serializers import RoomSerializer, PriceSerializer, UnavailableSerializer, LimitsSerializer, \
    ExtraSerializer, CustomerSerializer, BookingSerializer, ReportSerializer


class RoomListView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    # filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    # filterset_fields = ['check_in', 'check_out']
    # ordering_fields = ['id', 'prices']


class RoomDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class PriceListView(generics.ListCreateAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


class PriceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


class UnavailableListView(generics.ListCreateAPIView):
    queryset = Unavailable.objects.all()
    serializer_class = UnavailableSerializer


class UnavailableDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Unavailable.objects.all()
    serializer_class = UnavailableSerializer


class LimitsListView(generics.ListCreateAPIView):
    queryset = Limits.objects.all()
    serializer_class = LimitsSerializer


class LimitsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Limits.objects.all()
    serializer_class = LimitsSerializer


class ExtraListView(generics.ListCreateAPIView):
    queryset = Extra.objects.all()
    serializer_class = ExtraSerializer


class ExtraDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Extra.objects.all()
    serializer_class = ExtraSerializer


class CustomerListView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class BookingListView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class ReportListView(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class ReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

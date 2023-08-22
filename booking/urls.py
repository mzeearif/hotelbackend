# from django.urls import path
# from .views import ReservationListCreateView, RoomListCreateView, CustomerListCreateView, BookingListCreateView
#
# urlpatterns = [
#     path('reservations/', ReservationListCreateView.as_view(), name='reservation-list-create'),
#     path('rooms/', RoomListCreateView.as_view(), name='room-list-create'),
#     path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
#     path('bookings/', BookingListCreateView.as_view(), name='booking-list-create'),
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('rooms/', views.RoomListView.as_view(), name='room-list'),
    path('rooms/<int:pk>/', views.RoomDetailView.as_view(), name='room-detail'),
    path('prices/', views.PriceListView.as_view(), name='price-list'),
    path('prices/<int:pk>/', views.PriceDetailView.as_view(), name='price-detail'),
    path('unavailable/', views.UnavailableListView.as_view(), name='unavailable-list'),
    path('unavailable/<int:pk>/', views.UnavailableDetailView.as_view(), name='unavailable-detail'),
    path('limits/', views.LimitsListView.as_view(), name='limits-list'),
    path('limits/<int:pk>/', views.LimitsDetailView.as_view(), name='limits-detail'),
    path('extras/', views.ExtraListView.as_view(), name='extra-list'),
    path('extras/<int:pk>/', views.ExtraDetailView.as_view(), name='extra-detail'),
    path('customers/', views.CustomerListView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', views.CustomerDetailView.as_view(), name='customer-detail'),
    path('bookings/', views.BookingListView.as_view(), name='booking-list'),
    path('bookings/<int:pk>/', views.BookingDetailView.as_view(), name='booking-detail'),
    path('reports/', views.ReportListView.as_view(), name='report-list'),
    path('reports/<int:pk>/', views.ReportDetailView.as_view(), name='report-detail'),
]

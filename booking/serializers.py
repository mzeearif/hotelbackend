# from rest_framework import serializers
# from .models import Room, Customer, Booking
#
#
# class RoomSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Room
#         fields = ['id', 'name', 'no_of_rooms', 'adults', 'children', 'description', 'images', 'price', 'guest']
#
#
# class CustomerSerializer(serializers.ModelSerializer): class Meta: model = Customer fields = ['id', 'title',
# 'first_name', 'last_name', 'phone', 'email', 'arrival_time', 'additional_requirements']
#
#
# class BookingSerializer(serializers.ModelSerializer):
#     customer = CustomerSerializer()
#
#     room_type = RoomSerializer()
#
#     class Meta:
#         model = Booking
#         fields = ['id', 'customer', 'reservation', 'room_type']
#
#     def create(self, validated_data):
#         customer_data = validated_data.pop('customer')
#
#         room_type_data = validated_data.pop('room_type')
#
#         customer = Customer.objects.create(**customer_data)
#
#         room_type_id = room_type_data.get('id')  # Retrieve room_type_id if present
#         room_type = Room.objects.get(id=room_type_id) if room_type_id else None
#
#         total_rooms = room_type_data.get('no_of_rooms', 1)
#
#         price_per_room = room_type.price if room_type else 0
#         total_price = price_per_room * total_rooms
#
#         booking = Booking.objects.create(
#             customer=customer,
#             room_type=room_type,
#             total_rooms=total_rooms,
#             total_price=total_price,
#             **validated_data
#         )
#
#         return booking


from rest_framework import serializers
from .models import Room, Price, Unavailable, Limits, Extra, Customer, Booking, Report, RoomImage
from datetime import datetime


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'


class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ('image',)


class RoomSerializer(serializers.ModelSerializer):
    images = RoomImageSerializer(many=True, read_only=True)
    prices = serializers.SerializerMethodField()

    # prices = PriceSerializer(many=True, read_only=True, source='price_set')

    class Meta:
        model = Room
        fields = '__all__'

    def get_prices(self, obj):
        # Custom filter logic for Price objects based on your requirement
        # For example, to filter prices by a specific day, let's say 'Monday'

        # Get the current date and time
        current_date_time = datetime.now()

        # Get the day of the week as a string (e.g., 'Monday', 'Tuesday', etc.)
        current_day_of_week = current_date_time.strftime('%A')
        filtered_prices = obj.price_set.filter(day=current_day_of_week)
        return PriceSerializer(filtered_prices, many=True).data


class UnavailableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unavailable
        fields = '__all__'


class LimitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Limits
        fields = '__all__'


class ExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extra
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

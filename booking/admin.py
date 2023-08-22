from django.contrib import admin
# from django.utils.html import format_html
from django import forms
from django.utils.html import format_html

from .models import Room, Price, Unavailable, Limits, Extra, Customer, Booking, Report, RoomImage


# Register your models with their admin classes here

class PriceAdmin(admin.TabularInline):
    model = Price
    list_display = ('day', 'price_of_day', 'room_id')


class RoomImageInline(admin.TabularInline):  # You can also use StackedInline
    model = RoomImage
    extra = 1


class RoomAdmin(admin.ModelAdmin):
    inlines = [RoomImageInline, PriceAdmin]
    # inlines = [PriceAdmin]
    list_display = ('display_image', 'type', 'adults', 'children','max_occupancy', 'description', )

    def display_image(self, obj):
        if obj.images.exists():
            image_url = obj.images.first().image.url
            return format_html(f'<img src="{image_url}" alt="{obj.type}" style="max-width: 100px;"/>')
        return ''

    display_image.short_description = 'Image'
    # def display_image(self, obj):
    #     return format_html('<img src="{}" width="50" height="50" />', obj.images.url)
    #
    # display_image.short_description = 'Image'


class UnavailableAdmin(admin.ModelAdmin):
    list_display = ('room', 'type', 'date_from', 'date_to')


class LimitsAdmin(admin.ModelAdmin):
    list_display = ('room', 'start_on', 'date_from', 'date_to', 'min_night', 'max_night')


class ExtraAdmin(admin.ModelAdmin):
    list_display = ('name', 'per', 'price')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('title', 'first_name', 'last_name', 'phone', 'email', 'arrival_time', 'additional_requirements')


class BookingForm(forms.ModelForm):
    # adults = forms.IntegerField(label='Adults', min_value=1)
    # children = forms.IntegerField(label='Children', min_value=0)
    # room_count = forms.IntegerField(label='Room Count', min_value=1)

    class Meta:
        model = Booking
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)

        instance = kwargs.get('instance')
        if instance:
            # Set initial values from the model instance
            self.fields['adults'].initial = instance.adults
            self.fields['children'].initial = instance.children
            self.fields['room_count'].initial = instance.room_count


def get_extra_prices(obj):
    # Get the prices for the selected extras
    extra_prices = 0
    if obj.extra:
        for extra in obj.extra.all():
            extra_prices += int(extra.price)
    return extra_prices


class BookingAdmin(admin.ModelAdmin):
    form = BookingForm
    list_display = (
        'customer', 'arrival_date', 'arrival_time', 'departure_date', 'departure_time', 'adults', 'children', 'room',
        'room_count', 'get_selected_extras', 'price')

    def get_selected_extras(self, obj):
        if obj:
            obj.room.room_count -= obj.room_count
            # if obj.room_count ==0:
            #     obj.room.is_availabe = False
            obj.room.save()
        # Display the names of selected extras in the admin list view
        if obj.extra:
            return ", ".join(extra.name for extra in obj.extra.all())
        return ""

    def price(self, obj):
        # Calculate the total price based on the room count, price per room, and selected extras
        day = obj.arrival_time.strftime("%A")
        price = Price.objects.filter(day=day, room_id=obj.room.id).first()

        if price is not None:
            # Calculate the number of days between arrival and departure dates
            num_days = (obj.departure_date - obj.arrival_date).days + 1

            # Calculate the total price without extras
            total_price = int(price.price_of_day.replace('$', '')) * num_days * obj.room_count

            # Get the prices for the selected extras
            extra_prices = get_extra_prices(obj) * num_days

            # Add the extra prices to the total price
            total_price += extra_prices

            return f"${total_price}"

    get_selected_extras.short_description = 'Selected Extras'
    price.short_description = 'Total Price'


class ReportAdmin(admin.ModelAdmin):
    list_display = ('arrival_date', 'departure_date', 'booking')


# Register your models with their admin classes
admin.site.register(Room, RoomAdmin)
# admin.site.register(Price, PriceAdmin)
admin.site.register(Unavailable, UnavailableAdmin)
admin.site.register(Limits, LimitsAdmin)
admin.site.register(Extra, ExtraAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Report, ReportAdmin)

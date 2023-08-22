from django.db import models


# Create your models here.
class Room(models.Model):
    type = models.CharField(max_length=50)
    # ROOM_CHOICES = [(i, i) for i in range(1, 11)]
    room_count = models.IntegerField()
    adults = models.IntegerField(null=True, blank=True)
    children = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=500)
    # images = models.ImageField(upload_to='room_images/')
    max_occupancy = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.type}"


class RoomImage(models.Model):
    room = models.ForeignKey(Room, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='room_images/')

    def __str__(self):
        return f"Image for Room: {self.room.type}"


class Price(models.Model):
    DAYS_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    day = models.CharField(max_length=10, choices=DAYS_CHOICES)
    price_of_day = models.CharField(max_length=10)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.day}: ${self.price_of_day}"


class Unavailable(models.Model):
    UNAVAILABLE = 'unavailable'
    STOP_FOR_WEB = 'stop for web'
    EXTERNAL_BOOKING = 'external booking'
    TYPE_CHOICES = [
        (UNAVAILABLE, 'Unavailable'),
        (STOP_FOR_WEB, 'Stop for Web'),
        (EXTERNAL_BOOKING, 'External Booking'),
    ]

    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='unavailable')
    date_from = models.DateField()
    date_to = models.DateField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)

    def __str__(self):
        return f"{self.room.type} | {self.get_type_display()} | {self.date_from} to {self.date_to}"


class Limits(models.Model):
    DAYS_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date_from = models.DateField()
    date_to = models.DateField()
    start_on = models.CharField(max_length=10, choices=DAYS_CHOICES)
    min_night = models.IntegerField()
    max_night = models.IntegerField()

    def __str__(self):
        return f"{self.room.type} | {self.start_on} | {self.date_from} to {self.date_to}"


class Extra(models.Model):
    PER_CHOICES = [
        ('Per day', 'Per day'),
        ('Per person', 'Per person'),
        ('Per day / per person', 'Per day / per person'),
        ('Per booking', 'Per booking'),

    ]
    name = models.CharField(max_length=40)
    per = models.CharField(max_length=50, choices=PER_CHOICES)
    price = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"


class Customer(models.Model):
    TITLE_CHOICES = [
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Ms', 'Ms'),
        ('Miss', 'Miss'),
        ('Dr', 'Dr'),
    ]

    title = models.CharField(max_length=10, choices=TITLE_CHOICES)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    arrival_time = models.DateTimeField()
    additional_requirements = models.TextField()

    def __str__(self):
        return f"{self.first_name}"


class Booking(models.Model):
    arrival_date = models.DateField()
    arrival_time = models.DateTimeField()
    departure_date = models.DateField()
    departure_time = models.DateTimeField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    adults = models.IntegerField(null=True, blank=True)
    children = models.IntegerField(null=True, blank=True)
    room_count = models.IntegerField(default=1, null=False, blank=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    extra = models.ManyToManyField(Extra, blank=True)  # Update this line to ManyToManyField

    def __str__(self):
        return f"Booking {self.id}"

    # def __str__(
    #         self): return f"Customer: {self.customer},Room: {self.room.type},No-of-Room: {self.room.room_count}, " \
    #                       f"extra: {self.extra.name}"


class Report(models.Model):
    arrival_date = models.DateField()
    departure_date = models.DateField()
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.arrival_date}, {self.departure_date}"

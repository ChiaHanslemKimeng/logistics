from django.db import models
from django.conf import settings
import uuid
import datetime
import random

def generate_tracking_number():
    date_str = datetime.datetime.now().strftime('%Y%m%d')
    random_digits = ''.join([str(random.randint(0, 9)) for _ in range(4)])
    return f"CT{date_str}{random_digits}"

class Shipment(models.Model):
    class Country(models.TextChoices):
        USA = 'USA', 'United States'
        UK = 'UK', 'United Kingdom'
        CAN = 'CAN', 'Canada'
        DEU = 'DEU', 'Germany'
        FRA = 'FRA', 'France'
        ITA = 'ITA', 'Italy'
        ESP = 'ESP', 'Spain'
        CHN = 'CHN', 'China'
        JPN = 'JPN', 'Japan'
        IND = 'IND', 'India'
        AUS = 'AUS', 'Australia'
        BRA = 'BRA', 'Brazil'
        MEX = 'MEX', 'Mexico'
        ZAF = 'ZAF', 'South Africa'
        NGA = 'NGA', 'Nigeria'
        ARE = 'ARE', 'United Arab Emirates'
        SAU = 'SAU', 'Saudi Arabia'
        QAT = 'QAT', 'Qatar'
        TUR = 'TUR', 'Turkey'
        RUS = 'RUS', 'Russia'
        KOR = 'KOR', 'South Korea'
        SGP = 'SGP', 'Singapore'

    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('PICKED_UP', 'Picked Up'),
        ('IN_TRANSIT', 'In Transit'),
        ('ARRIVED_FACILITY', 'Arrived at Facility'),
        ('CUSTOMS', 'Customs Clearance'),
        ('OUT_FOR_DELIVERY', 'Out for Delivery'),
        ('DELIVERED', 'Delivered'),
        ('FAILED', 'Failed Delivery'),
    )

    MODE_CHOICES = (
        ('AIR', 'Air Freight'),
        ('SEA', 'Sea Freight'),
        ('ROAD', 'Road Transport'),
        ('RAIL', 'Rail Transport'),
    )

    tracking_number = models.CharField(max_length=20, unique=True, default=generate_tracking_number)
    
    # Sender Info
    sender_name = models.CharField(max_length=255)
    sender_email = models.EmailField()
    sender_phone = models.CharField(max_length=20)
    
    # Receiver Info
    receiver_name = models.CharField(max_length=255)
    receiver_email = models.EmailField()
    receiver_phone = models.CharField(max_length=20)
    
    # Parcel Info
    product = models.CharField(max_length=255, default="General Logistics")
    quantity = models.PositiveIntegerField(default=1)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    shipment_type = models.CharField(max_length=100) # e.g. Express, Standard
    shipment_mode = models.CharField(max_length=20, choices=MODE_CHOICES, default='AIR')
    carrier = models.CharField(max_length=100, default="Global Courier Internal")
    description = models.TextField(blank=True, null=True)
    
    # Route Info
    origin_country = models.CharField(max_length=100, choices=Country.choices)
    origin_city = models.CharField(max_length=100)
    destination_country = models.CharField(max_length=100, choices=Country.choices)
    destination_city = models.CharField(max_length=100)
    
    # Timing
    departure_time = models.DateTimeField(null=True, blank=True)
    estimated_delivery_date = models.DateField()
    
    # Current Status
    current_country = models.CharField(max_length=100, choices=Country.choices)
    current_city = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    comment = models.TextField(blank=True, null=True, help_text="Internal staff comments")
    
    # Metadata
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='created_shipments')
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_shipments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.tracking_number} - {self.status}"

class Package(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, related_name='packages')
    package_id = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    dimensions = models.CharField(max_length=100, help_text="L x W x H (cm)", blank=True, null=True)
    status = models.CharField(max_length=50, default="In Progress")

    def __str__(self):
        return f"Package {self.package_id} (Shipment: {self.shipment.tracking_number})"

class ShipmentHistory(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, related_name='history')
    status = models.CharField(max_length=20, choices=Shipment.STATUS_CHOICES)
    location_country = models.CharField(max_length=100, choices=Shipment.Country.choices)
    location_city = models.CharField(max_length=100)
    remarks = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.shipment.tracking_number} - {self.status} at {self.location_city}"

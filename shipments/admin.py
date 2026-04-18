from django.contrib import admin
from django.db import models
from django.forms import Select
from .models import Shipment, ShipmentHistory, Package

class ShipmentHistoryInline(admin.TabularInline):
    model = ShipmentHistory
    extra = 1
    fields = ('status', 'location_country', 'location_city', 'remarks', 'timestamp')
    readonly_fields = ('timestamp',)
    formfield_overrides = {
        models.CharField: {'widget': Select},
    }

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('package_id', 'shipment', 'weight', 'status')
    search_fields = ('package_id', 'shipment__tracking_number')

class PackageInline(admin.TabularInline):
    model = Package
    extra = 1
    fields = ('package_id', 'description', 'weight', 'dimensions', 'status')

from django.forms import Select

@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('tracking_number', 'sender_name', 'receiver_name', 'carrier', 'status', 'estimated_delivery_date')
    list_filter = ('status', 'shipment_mode', 'carrier', 'origin_country', 'destination_country', 'created_at')
    search_fields = ('tracking_number', 'sender_name', 'receiver_name', 'product')
    inlines = [PackageInline, ShipmentHistoryInline]
    date_hierarchy = 'created_at'
    
    # Explicitly force dropdowns for country fields
    formfield_overrides = {
        models.CharField: {'widget': Select},
    }
    
    fieldsets = (
        ('Shipment Identity', {
            'fields': ('tracking_number', 'status', 'carrier', 'shipment_mode', 'product', 'quantity')
        }),
        ('Timing', {
            'fields': ('departure_time', 'estimated_delivery_date')
        }),
        ('Sender Details', {
            'fields': ('sender_name', 'sender_email', 'sender_phone')
        }),
        ('Receiver Details', {
            'fields': ('receiver_name', 'receiver_email', 'receiver_phone')
        }),
        ('Parcel Route', {
            'fields': ('weight', 'shipment_type', 'origin_country', 'origin_city', 'destination_country', 'destination_city')
        }),
        ('Current Location', {
            'fields': ('current_country', 'current_city')
        }),
        ('Administration', {
            'fields': ('created_by', 'assigned_to', 'comment')
        }),
    )
    readonly_fields = ('tracking_number',)

@admin.register(ShipmentHistory)
class ShipmentHistoryAdmin(admin.ModelAdmin):
    list_display = ('shipment', 'status', 'location_city', 'timestamp')
    list_filter = ('status', 'location_country', 'timestamp')
    search_fields = ('shipment__tracking_number',)
    formfield_overrides = {
        models.CharField: {'widget': Select},
    }

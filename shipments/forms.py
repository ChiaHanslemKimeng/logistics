from django import forms
from .models import Shipment

class ShipmentForm(forms.ModelForm):
    class Meta:
        model = Shipment
        exclude = ('tracking_number', 'created_by', 'created_at', 'updated_at')
        widgets = {
            'estimated_delivery_date': forms.DateInput(attrs={'type': 'date', 'class': 'input input-bordered w-full rounded-xl'}),
            'sender_name': forms.TextInput(attrs={'class': 'input input-bordered w-full rounded-xl'}),
            'sender_email': forms.EmailInput(attrs={'class': 'input input-bordered w-full rounded-xl'}),
            'sender_phone': forms.TextInput(attrs={'class': 'input input-bordered w-full rounded-xl'}),
            'receiver_name': forms.TextInput(attrs={'class': 'input input-bordered w-full rounded-xl'}),
            'receiver_email': forms.EmailInput(attrs={'class': 'input input-bordered w-full rounded-xl'}),
            'receiver_phone': forms.TextInput(attrs={'class': 'input input-bordered w-full rounded-xl'}),
            'description': forms.Textarea(attrs={'class': 'textarea textarea-bordered w-full rounded-xl', 'rows': 3}),
            'weight': forms.NumberInput(attrs={'class': 'input input-bordered w-full rounded-xl'}),
            'shipment_type': forms.TextInput(attrs={'class': 'input input-bordered w-full rounded-xl'}),
            'origin_country': forms.TextInput(attrs={'class': 'input input-bordered w-full rounded-xl'}),
            'origin_city': forms.TextInput(attrs={'class': 'input input-bordered w-full rounded-xl'}),
            'destination_country': forms.TextInput(attrs={'class': 'input input-bordered w-full rounded-xl'}),
            'destination_city': forms.TextInput(attrs={'class': 'input input-bordered w-full rounded-xl'}),
            'current_country': forms.TextInput(attrs={'class': 'input input-bordered w-full rounded-xl'}),
            'current_city': forms.TextInput(attrs={'class': 'input input-bordered w-full rounded-xl'}),
            'status': forms.Select(attrs={'class': 'select select-bordered w-full rounded-xl'}),
            'assigned_to': forms.Select(attrs={'class': 'select select-bordered w-full rounded-xl'}),
        }

class ShipmentUpdateForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = ('status', 'current_country', 'current_city')
        widgets = {
            'status': forms.Select(attrs={'class': 'select select-bordered w-full rounded-xl shadow-sm'}),
            'current_country': forms.TextInput(attrs={'class': 'input input-bordered w-full rounded-xl shadow-sm'}),
            'current_city': forms.TextInput(attrs={'class': 'input input-bordered w-full rounded-xl shadow-sm'}),
        }

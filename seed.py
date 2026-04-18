import os
import django
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'logistics_system.settings')
django.setup()

from django.contrib.auth import get_user_model
from shipments.models import Shipment, ShipmentHistory

User = get_user_model()

def seed_data():
    # Create Super Admin
    if not User.objects.filter(username='admin').exists():
        admin = User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        admin.role = 'SUPER_ADMIN'
        admin.save()
        print("Super Admin created: admin/admin123")

    # Create Staff
    if not User.objects.filter(username='staff1').exists():
        staff = User.objects.create_user('staff1', 'staff1@example.com', 'staff123')
        staff.role = 'STAFF'
        staff.first_name = 'John'
        staff.last_name = 'Doe'
        staff.save()
        print("Staff created: staff1/staff123")
    else:
        staff = User.objects.get(username='staff1')

    # Create a sample shipment
    if not Shipment.objects.exists():
        shipment = Shipment.objects.create(
            sender_name="Alice Smith",
            sender_email="alice@example.com",
            sender_phone="+123456789",
            receiver_name="Bob Brown",
            receiver_email="bob@example.com",
            receiver_phone="+987654321",
            description="MacBook Pro 16 inch",
            weight=2.5,
            shipment_type="Express Air",
            origin_country="USA",
            origin_city="New York",
            destination_country="Nigeria",
            destination_city="Lagos",
            current_country="USA",
            current_city="New York",
            status="PICKED_UP",
            estimated_delivery_date=datetime.date.today() + datetime.timedelta(days=7),
            created_by=staff,
            assigned_to=staff
        )
        print(f"Sample shipment created: {shipment.tracking_number}")

if __name__ == '__main__':
    seed_data()

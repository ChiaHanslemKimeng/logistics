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
        AFG = 'AFG', 'Afghanistan'
        ALB = 'ALB', 'Albania'
        DZA = 'DZA', 'Algeria'
        AND = 'AND', 'Andorra'
        AGO = 'AGO', 'Angola'
        ATG = 'ATG', 'Antigua and Barbuda'
        ARG = 'ARG', 'Argentina'
        ARM = 'ARM', 'Armenia'
        AUS = 'AUS', 'Australia'
        AUT = 'AUT', 'Austria'
        AZE = 'AZE', 'Azerbaijan'
        BHS = 'BHS', 'Bahamas'
        BHR = 'BHR', 'Bahrain'
        BGD = 'BGD', 'Bangladesh'
        BRB = 'BRB', 'Barbados'
        BLR = 'BLR', 'Belarus'
        BEL = 'BEL', 'Belgium'
        BLZ = 'BLZ', 'Belize'
        BEN = 'BEN', 'Benin'
        BTN = 'BTN', 'Bhutan'
        BOL = 'BOL', 'Bolivia'
        BIH = 'BIH', 'Bosnia and Herzegovina'
        BWA = 'BWA', 'Botswana'
        BRA = 'BRA', 'Brazil'
        BRN = 'BRN', 'Brunei'
        BGR = 'BGR', 'Bulgaria'
        BFA = 'BFA', 'Burkina Faso'
        BDI = 'BDI', 'Burundi'
        CPV = 'CPV', 'Cabo Verde'
        KHM = 'KHM', 'Cambodia'
        CMR = 'CMR', 'Cameroon'
        CAN = 'CAN', 'Canada'
        CAF = 'CAF', 'Central African Republic'
        TCD = 'TCD', 'Chad'
        CHL = 'CHL', 'Chile'
        CHN = 'CHN', 'China'
        COL = 'COL', 'Colombia'
        COM = 'COM', 'Comoros'
        COD = 'COD', 'Congo (DRC)'
        COG = 'COG', 'Congo (Republic)'
        CRI = 'CRI', 'Costa Rica'
        HRV = 'HRV', 'Croatia'
        CUB = 'CUB', 'Cuba'
        CYP = 'CYP', 'Cyprus'
        CZE = 'CZE', 'Czech Republic'
        DNK = 'DNK', 'Denmark'
        DJI = 'DJI', 'Djibouti'
        DOM = 'DOM', 'Dominican Republic'
        ECU = 'ECU', 'Ecuador'
        EGY = 'EGY', 'Egypt'
        SLV = 'SLV', 'El Salvador'
        GNQ = 'GNQ', 'Equatorial Guinea'
        ERI = 'ERI', 'Eritrea'
        EST = 'EST', 'Estonia'
        SWZ = 'SWZ', 'Eswatini'
        ETH = 'ETH', 'Ethiopia'
        FJI = 'FJI', 'Fiji'
        FIN = 'FIN', 'Finland'
        FRA = 'FRA', 'France'
        GAB = 'GAB', 'Gabon'
        GMB = 'GMB', 'Gambia'
        GEO = 'GEO', 'Georgia'
        DEU = 'DEU', 'Germany'
        GHA = 'GHA', 'Ghana'
        GRC = 'GRC', 'Greece'
        GRD = 'GRD', 'Grenada'
        GTM = 'GTM', 'Guatemala'
        GIN = 'GIN', 'Guinea'
        GNB = 'GNB', 'Guinea-Bissau'
        GUY = 'GUY', 'Guyana'
        HTI = 'HTI', 'Haiti'
        HND = 'HND', 'Honduras'
        HUN = 'HUN', 'Hungary'
        ISL = 'ISL', 'Iceland'
        IND = 'IND', 'India'
        IDN = 'IDN', 'Indonesia'
        IRN = 'IRN', 'Iran'
        IRQ = 'IRQ', 'Iraq'
        IRL = 'IRL', 'Ireland'
        ISR = 'ISR', 'Israel'
        ITA = 'ITA', 'Italy'
        JAM = 'JAM', 'Jamaica'
        JPN = 'JPN', 'Japan'
        JOR = 'JOR', 'Jordan'
        KAZ = 'KAZ', 'Kazakhstan'
        KEN = 'KEN', 'Kenya'
        KIR = 'KIR', 'Kiribati'
        KWT = 'KWT', 'Kuwait'
        KGZ = 'KGZ', 'Kyrgyzstan'
        LAO = 'LAO', 'Laos'
        LVA = 'LVA', 'Latvia'
        LBN = 'LBN', 'Lebanon'
        LSO = 'LSO', 'Lesotho'
        LBR = 'LBR', 'Liberia'
        LBY = 'LBY', 'Libya'
        LIE = 'LIE', 'Liechtenstein'
        LTU = 'LTU', 'Lithuania'
        LUX = 'LUX', 'Luxembourg'
        MDG = 'MDG', 'Madagascar'
        MWI = 'MWI', 'Malawi'
        MYS = 'MYS', 'Malaysia'
        MDV = 'MDV', 'Maldives'
        MLI = 'MLI', 'Mali'
        MLT = 'MLT', 'Malta'
        MRT = 'MRT', 'Mauritania'
        MUS = 'MUS', 'Mauritius'
        MEX = 'MEX', 'Mexico'
        MDA = 'MDA', 'Moldova'
        MNG = 'MNG', 'Mongolia'
        MNE = 'MNE', 'Montenegro'
        MAR = 'MAR', 'Morocco'
        MOZ = 'MOZ', 'Mozambique'
        MMR = 'MMR', 'Myanmar'
        NAM = 'NAM', 'Namibia'
        NPL = 'NPL', 'Nepal'
        NLD = 'NLD', 'Netherlands'
        NZL = 'NZL', 'New Zealand'
        NIC = 'NIC', 'Nicaragua'
        NER = 'NER', 'Niger'
        NGA = 'NGA', 'Nigeria'
        PRK = 'PRK', 'North Korea'
        MKD = 'MKD', 'North Macedonia'
        NOR = 'NOR', 'Norway'
        OMN = 'OMN', 'Oman'
        PAK = 'PAK', 'Pakistan'
        PAN = 'PAN', 'Panama'
        PNG = 'PNG', 'Papua New Guinea'
        PRY = 'PRY', 'Paraguay'
        PER = 'PER', 'Peru'
        PHL = 'PHL', 'Philippines'
        POL = 'POL', 'Poland'
        PRT = 'PRT', 'Portugal'
        QAT = 'QAT', 'Qatar'
        ROU = 'ROU', 'Romania'
        RUS = 'RUS', 'Russia'
        RWA = 'RWA', 'Rwanda'
        KNA = 'KNA', 'Saint Kitts and Nevis'
        LCA = 'LCA', 'Saint Lucia'
        VCT = 'VCT', 'Saint Vincent and the Grenadines'
        WSM = 'WSM', 'Samoa'
        STP = 'STP', 'Sao Tome and Principe'
        SAU = 'SAU', 'Saudi Arabia'
        SEN = 'SEN', 'Senegal'
        SRB = 'SRB', 'Serbia'
        SLE = 'SLE', 'Sierra Leone'
        SGP = 'SGP', 'Singapore'
        SVK = 'SVK', 'Slovakia'
        SVN = 'SVN', 'Slovenia'
        SLB = 'SLB', 'Solomon Islands'
        SOM = 'SOM', 'Somalia'
        ZAF = 'ZAF', 'South Africa'
        SSD = 'SSD', 'South Sudan'
        KOR = 'KOR', 'South Korea'
        ESP = 'ESP', 'Spain'
        LKA = 'LKA', 'Sri Lanka'
        SDN = 'SDN', 'Sudan'
        SUR = 'SUR', 'Suriname'
        SWE = 'SWE', 'Sweden'
        CHE = 'CHE', 'Switzerland'
        SYR = 'SYR', 'Syria'
        TWN = 'TWN', 'Taiwan'
        TJK = 'TJK', 'Tajikistan'
        TZA = 'TZA', 'Tanzania'
        THA = 'THA', 'Thailand'
        TLS = 'TLS', 'Timor-Leste'
        TGO = 'TGO', 'Togo'
        TON = 'TON', 'Tonga'
        TTO = 'TTO', 'Trinidad and Tobago'
        TUN = 'TUN', 'Tunisia'
        TUR = 'TUR', 'Turkey'
        TKM = 'TKM', 'Turkmenistan'
        TUV = 'TUV', 'Tuvalu'
        UGA = 'UGA', 'Uganda'
        UKR = 'UKR', 'Ukraine'
        ARE = 'ARE', 'United Arab Emirates'
        UK = 'UK', 'United Kingdom'
        USA = 'USA', 'United States'
        URY = 'URY', 'Uruguay'
        UZB = 'UZB', 'Uzbekistan'
        VUT = 'VUT', 'Vanuatu'
        VEN = 'VEN', 'Venezuela'
        VNM = 'VNM', 'Vietnam'
        YEM = 'YEM', 'Yemen'
        ZMB = 'ZMB', 'Zambia'
        ZWE = 'ZWE', 'Zimbabwe'

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

    CARRIER_CHOICES = (
        ('FLEET_DIRECT', 'Fleet Direct Internal'),
        ('DHL', 'DHL Express'),
        ('FEDEX', 'FedEx'),
        ('UPS', 'UPS'),
        ('ARAMEX', 'Aramex'),
        ('TNT', 'TNT'),
        ('USPS', 'USPS'),
        ('ROYAL_MAIL', 'Royal Mail'),
        ('CANADA_POST', 'Canada Post'),
        ('AUSTRALIA_POST', 'Australia Post'),
        ('SF_EXPRESS', 'SF Express'),
        ('EMS', 'EMS'),
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
    carrier = models.CharField(max_length=100, choices=CARRIER_CHOICES, default='FLEET_DIRECT')
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

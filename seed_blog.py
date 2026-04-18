import os
import django
import datetime
from django.utils.text import slugify

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'logistics_system.settings')
django.setup()

from core.models import BlogPost

def seed_blog():
    posts_data = [
        {
            "title": "The Future of Global Logistics in 2026",
            "content": "As we move further into 2026, the logistics industry is witnessing a massive transformation driven by AI and automation. From drone deliveries to predictive supply chain management, the way we move goods is changing forever...",
        },
        {
            "title": "5 Tips for Faster International Shipping",
            "content": "International shipping can be complex, but with the right preparation, you can significantly reduce transit times. Ensure all documentation is accurate, choose the right shipping partner, and understand customs regulations...",
        },
        {
            "title": "Understanding Customs Clearance: A Complete Guide",
            "content": "Customs clearance is often the most misunderstood part of the shipping process. In this guide, we break down the essential steps to ensure your parcel passes through customs without delays...",
        },
        {
            "title": "Why Sustainable Packaging Matters for Your Business",
            "content": "Eco-friendly shipping is no longer just a trend; it's a necessity. Businesses that adopt sustainable packaging solutions not only help the environment but also build stronger brand loyalty with conscious consumers...",
        },
        {
            "title": "How to Track Your Shipment Like a Pro",
            "content": "Real-time tracking is a game-changer. Learn how to use our advanced tracking portal to monitor your shipment's journey from origin to destination with precision...",
        },
        {
            "title": "The Rise of E-commerce Logistics in Africa",
            "content": "The African e-commerce market is booming, and with it, the demand for reliable logistics. We explore the challenges and opportunities in delivering across the continent...",
        },
        {
            "title": "Air Freight vs. Sea Freight: Which is Right for You?",
            "content": "Choosing between air and sea freight depends on your budget, timeline, and the nature of your goods. We compare both options to help you make an informed decision...",
        },
        {
            "title": "Protecting High-Value Goods During Transit",
            "content": "Shipping expensive electronics or luxury items requires special care. Learn about our specialized security protocols and insurance options for high-value shipments...",
        },
        {
            "title": "The Importance of Last-Mile Delivery Excellence",
            "content": "The final leg of the journey is often the most critical. Discover how we optimize last-mile delivery to ensure your customers receive their parcels on time, every time...",
            
        },
        {
            "title": "Innovations in Automated Warehousing",
            "content": "Automation is revolutionizing the warehouse. From autonomous robots to smart sorting systems, see how we use technology to process shipments faster than ever before...",
        }
    ]

    for data in posts_data:
        if not BlogPost.objects.filter(title=data['title']).exists():
            BlogPost.objects.create(
                title=data['title'],
                slug=slugify(data['title']),
                content=data['content'],
                author="Global Courier Team"
            )
            print(f"Blog post created: {data['title']}")

if __name__ == '__main__':
    seed_blog()

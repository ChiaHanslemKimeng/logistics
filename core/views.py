from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import BlogPost, Review
from shipments.models import Shipment
from .forms import ReviewForm

def home(request):
    featured_posts = BlogPost.objects.all()[:3]
    latest_reviews = Review.objects.filter(is_approved=True)[:5]
    return render(request, 'core/home.html', {
        'featured_posts': featured_posts,
        'latest_reviews': latest_reviews
    })

def reviews_view(request):
    reviews = Review.objects.filter(is_approved=True)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! Your review has been submitted and is awaiting moderation.')
            return redirect('reviews')
    else:
        form = ReviewForm()
    
    return render(request, 'core/reviews.html', {
        'reviews': reviews,
        'form': form
    })

def services(request):
    return render(request, 'core/services.html')

def about(request):
    return render(request, 'core/about.html')

from django.core.mail import send_mail
from django.conf import settings

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        if name and email and message:
            try:
                # Send email to Admin
                full_subject = f"Contact Form: {subject} from {name}"
                full_message = f"Sender Name: {name}\nSender Email: {email}\n\nMessage:\n{message}"
                
                send_mail(
                    full_subject,
                    full_message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.ADMIN_EMAIL],
                    fail_silently=False,
                )
                messages.success(request, 'Your message has been sent successfully. We will get back to you shortly!')
            except Exception as e:
                messages.error(request, 'Failed to send message. Please try again later.')
                print(f"Contact email error: {e}")
        else:
            messages.error(request, 'Please fill in all required fields.')
            
        return redirect('contact')
        
    return render(request, 'core/contact.html')

def blog_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'core/blog_list.html', {'posts': posts})

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'core/blog_detail.html', {'post': post})

def tracking(request):
    return render(request, 'core/tracking.html')

def tracking_result(request):
    tracking_number = request.GET.get('number')
    shipment = None
    if tracking_number:
        try:
            shipment = Shipment.objects.get(tracking_number=tracking_number)
        except Shipment.DoesNotExist:
            shipment = None
            
    return render(request, 'core/tracking_result.html', {
        'shipment': shipment,
        'tracking_number': tracking_number
    })

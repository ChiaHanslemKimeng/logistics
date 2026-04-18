from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from shipments.models import Shipment

@login_required
def dashboard(request):
    search_query = request.GET.get('q', '')
    
    if request.user.role == 'SUPER_ADMIN' or request.user.is_superuser:
        shipments = Shipment.objects.all().order_by('-created_at')
        if search_query:
            shipments = shipments.filter(tracking_number__icontains=search_query)
            
        total = shipments.count()
        delivered = shipments.filter(status='DELIVERED').count()
        pending = shipments.filter(status='PENDING').count()
        
        # Get recent activity logs
        from .models import ActivityLog
        logs = ActivityLog.objects.all().select_related('user')[:10]
        
        return render(request, 'users/admin_dashboard.html', {
            'shipments': shipments,
            'total': total,
            'delivered': delivered,
            'pending': pending,
            'logs': logs,
            'search_query': search_query
        })
    else:
        shipments = Shipment.objects.filter(assigned_to=request.user).order_by('-created_at')
        if search_query:
            shipments = shipments.filter(tracking_number__icontains=search_query)
            
        return render(request, 'users/staff_dashboard.html', {
            'shipments': shipments,
            'search_query': search_query
        })

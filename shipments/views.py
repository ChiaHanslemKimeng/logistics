from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Shipment
from .forms import ShipmentForm, ShipmentUpdateForm

@login_required
def create_shipment(request):
    if request.method == 'POST':
        form = ShipmentForm(request.POST)
        if form.is_valid():
            shipment = form.save(commit=False)
            shipment.created_by = request.user
            shipment.save()
            return redirect('dashboard')
    else:
        form = ShipmentForm()
    return render(request, 'shipments/shipment_form.html', {'form': form, 'title': 'Create New Shipment'})

@login_required
def update_shipment(request, pk):
    shipment = get_object_or_404(Shipment, pk=pk)
    # Check permissions: Only Super Admin or assigned Staff
    if not (request.user.role == 'SUPER_ADMIN' or request.user.is_superuser or shipment.assigned_to == request.user):
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = ShipmentUpdateForm(request.POST, instance=shipment)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ShipmentUpdateForm(instance=shipment)
    return render(request, 'shipments/shipment_update.html', {'form': form, 'shipment': shipment})

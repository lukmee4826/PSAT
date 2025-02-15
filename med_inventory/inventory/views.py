from django.shortcuts import render
from django.db.models import Sum
from .models import Medicine, Requisition
from django.contrib.auth.models import User
from .forms import MedicineForm

# Dashboard View
def dashboard(request):
    # Total Medicines
    total_medicines = Medicine.objects.count()

    # Expiring Medicines (example: medicines expiring in the next 30 days)
    expiring_medicines = Medicine.objects.filter(expiration_date__lt="2025-03-15").count()

    # Recent Requisitions (example: last 5 requisitions)
    recent_requisitions = Requisition.objects.order_by('-date_created')[:5]

    # Low stock medicines (example: medicines with quantity below 10)
    low_stock_items = Medicine.objects.filter(quantity__lt=10)

    # Render Dashboard Template with data
    context = {
        'total_medicines': total_medicines,
        'expiring_medicines': expiring_medicines,
        'recent_requisitions': recent_requisitions,
        'low_stock_items': low_stock_items,
    }
    return render(request, 'dashboard.html', context)

# Inventory List View
def inventory_list(request):
    medicines = Medicine.objects.all()
    return render(request, 'inventory/inventory_list.html', {'medicines': medicines})

# Add Medicine View
def add_medicine(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = MedicineForm()
    return render(request, 'inventory/add_medicine.html', {'form': form})

# Edit Medicine View
def edit_medicine(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    if request.method == 'POST':
        form = MedicineForm(request.POST, instance=medicine)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = MedicineForm(instance=medicine)
    return render(request, 'inventory/edit_medicine.html', {'form': form})

# Delete Medicine View
def delete_medicine(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    if request.method == 'POST':
        medicine.delete()
        return redirect('inventory_list')
    return render(request, 'inventory/delete_medicine.html', {'medicine': medicine})

# Requisition Management View (for managing requisition requests)
def requisition_list(request):
    requisitions = Requisition.objects.all()
    return render(request, 'requisition/requisition_list.html', {'requisitions': requisitions})

# User Management View (to manage users in the system)
def user_management(request):
    users = User.objects.all()
    return render(request, 'user_management/user_management_list.html', {'users': users})

# Forecasting & Analytics (for showing forecasting trends)
def forecasting(request):
    # Add forecasting logic here (for simplicity, returning dummy data)
    data = {'forecast': "Trend data goes here"}
    return render(request, 'forecasting/forecasting.html', data)

# Loan & Borrowing Management View
def loan_borrowing(request):
    # Loan and Borrowing logic can be added here
    return render(request, 'loan_borrowing/loan_borrowing.html')

# Alerts & Notifications View
def alerts(request):
    # Alerts logic here (you can use Django messages or any other alert system)
    alerts_data = {'alerts': "Alert messages go here"}
    return render(request, 'alerts/alerts.html', alerts_data)

def requisition(request):
    # Fetch requisition data (you can modify this to include necessary logic)
    requisitions = Requisition.objects.all()  # Example: fetch all requisitions
    return render(request, 'requisition.html', {'requisitions': requisitions})

def forecasting(request):
    # Implement forecasting logic, e.g., fetching data based on usage
    return render(request, 'forecasting.html')

def user_management(request):
    # Fetch users for user management page
    users = User.objects.all()
    return render(request, 'user_management.html', {'users': users})
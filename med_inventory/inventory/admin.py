from django.contrib import admin
from .models import Medicine

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity', 'expiration_date', 'is_expiring_soon')
    list_filter = ('category', 'expiration_date')
    search_fields = ('name',)

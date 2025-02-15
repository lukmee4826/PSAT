from django.db import models
from django.utils import timezone

class Medicine(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    quantity = models.IntegerField()
    expiration_date = models.DateField()
    supplier = models.CharField(max_length=255, blank=True, null=True)

    def is_expiring_soon(self):
        from datetime import date, timedelta
        return self.expiration_date <= date.today() + timedelta(days=30)

    def __str__(self):
        return self.name

class Requisition(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity_requested = models.IntegerField()
    date_created = models.DateTimeField(default=timezone.now)
    requestor = models.CharField(max_length=200)  # You can adjust this field as needed

    def __str__(self):
        return f"Requisition for {self.medicine.name} by {self.requestor}"